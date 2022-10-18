resource rockset_workspace community {
  name = "community"
}

resource rockset_kafka_integration confluent {
  name              = "confluent-cloud"
  description       = "Integration to ingest documents from Confluent Cloud"
  use_v3            = true
  bootstrap_servers = var.KAFKA_REST_ENDPOINT
  security_config   = {
    api_key = var.KAFKA_API_KEY
    secret  = var.KAFKA_API_SECRET
  }
}

resource rockset_kafka_collection orders {
  name           = "orders"
  workspace      = rockset_workspace.community.name
  description    = "Ingestion of sample data from Confluent Cloud."
  retention_secs = 3600
  insert_only    = true

  source {
    integration_name    = rockset_kafka_integration.confluent.name
    use_v3              = true
    topic_name          = "test_json"
    offset_reset_policy = "EARLIEST"
  }
  field_mapping_query = file("sql/ingest-transformation.sql")
}

resource rockset_alias production {
  collections = ["${rockset_workspace.community.name}.${rockset_kafka_collection.orders.name}"]
  name        = "production"
  workspace   = rockset_workspace.community.name
}

resource rockset_s3_integration public {
  name         = "rockset-public-collections"
  description  = "Integration to access Rockset's public datasets"
  aws_role_arn = "arn:aws:iam::469279130686:role/rockset-public-datasets"
}

resource rockset_s3_collection cities {
  description = "This collection contains sample data from the Rockset public dataset from S3"
  workspace   = rockset_workspace.community.name
  name        = "cities"

  source {
    integration_name = rockset_s3_integration.public.name
    bucket           = "rockset-public-datasets"
    pattern          = "cities/geonames-all-cities-with-a-population-1000.json"
    format           = "json"
  }
}

resource rockset_role query-only {
  name        = "query-only"
  description = "This role can only query collections in the ${rockset_workspace.community.name} workspace in the usw2a1 cluster"

  privilege {
    action        = "QUERY_DATA_WS"
    resource_name = rockset_workspace.community.name
    cluster       = "usw2a1"
  }
  privilege {
    action        = "EXECUTE_QUERY_LAMBDA_WS"
    resource_name = rockset_workspace.community.name
    cluster       = "usw2a1"
  }
}

resource rockset_api_key query-only {
  name = "query-only"
  role = rockset_role.query-only.name
}

resource rockset_query_lambda orders-summary {
  name      = "orders-summary"
  workspace = rockset_workspace.community.name
  sql {
    query = templatefile("sql/orders-summary.sql.tftpl",
      {
        workspace  = rockset_workspace.community.name,
        collection = rockset_alias.production.name
        states     = var.states
      })
  }
}

resource "rockset_query_lambda_tag" "production" {
  workspace    = rockset_workspace.community.name
  name         = "production"
  query_lambda = rockset_query_lambda.orders-summary.name
  version      = var.production_version == "" ? rockset_query_lambda.orders-summary.version : var.production_version
}

resource rockset_view state {
  count       = length(var.states)
  name        = var.states[count.index]
  description = "limit the view of the data to ${var.states[count.index]}"
  workspace   = rockset_workspace.community.name
  query       = templatefile("sql/view.sql.tftpl",
    {
      workspace  = rockset_workspace.community.name,
      collection = rockset_alias.production.name,
      state      = var.states[count.index]
    })
}
