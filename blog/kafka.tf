resource "rockset_kafka_integration" "confluent" {
  name              = "confluent-cloud-blog"
  use_v3            = true
  bootstrap_servers = var.KAFKA_REST_ENDPOINT
  security_config   = {
    api_key = var.KAFKA_API_KEY
    secret  = var.KAFKA_API_SECRET
  }
}

resource "rockset_kafka_collection" "orders" {
  name           = "orders"
  workspace      = rockset_workspace.blog.name
  retention_secs = var.retention_secs
  source {
    integration_name    = rockset_kafka_integration.confluent.name
    topic_name          = "test_json"
    use_v3              = true
    offset_reset_policy = "EARLIEST"
  }
  field_mapping_query = file("data/transformation.sql")
}
