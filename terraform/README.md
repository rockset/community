# Terraform for Rockset

This directory contains sample terraform configs to configure a Rockset organization with a couple of
collections.



## Installation

All you need to try this out is terraform, which you can download from the 
[Hashicorp site](https://www.terraform.io/downloads)
or through 
[homebrew](https://brew.sh).

```bash
$ brew install terraform
```

### Rockset API key

You also need a Rockset API key, which you get from the 
[Rockset console](https://console.rockset.com/apikeys),
and the Rockset API server you want to use, e.g.
* `https://api.usw2a1.rockset.com/` for the AWS `us-west-2` region
* `https://api.use1a1.rockset.com/` for the AWS `us-east-1` region
* `https://api.euc1a1.rockset.com/` for the AWS `eu-central-1` region

These should be set as environment variables to avoid storing secrets in configuration files, e.g.

```bash
$ export ROCKSET_APIKEY='e9GH...7kTF'
$ export ROCKSET_APISERVER='https://api.usw2a1.rockset.com/' 
```

These will be picked up by the terraform provider.

## Initial apply

When you apply this configuration the first time, 

```bash
$ terraform init
```

```bash
$ terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

...

  # rockset_workspace.community will be created
  + resource "rockset_workspace" "community" {
      + created_by  = (known after apply)
      + description = "created by Rockset terraform provider"
      + id          = (known after apply)
      + name        = "community"
    }

Plan: 12 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value:
```

<details>
  <summary>Full terraform output</summary>

```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

# rockset_alias.production will be created
+ resource "rockset_alias" "production" {
    + collections = [
        + "community.orders",
          ]
    + description = "created by Rockset terraform provider"
    + id          = (known after apply)
    + name        = "production"
    + workspace   = "community"
      }

# rockset_api_key.query-only will be created
+ resource "rockset_api_key" "query-only" {
    + id   = (known after apply)
    + key  = (sensitive value)
    + name = "query-only"
    + role = "query-only"
    + user = (known after apply)
      }

# rockset_kafka_collection.orders will be created
+ resource "rockset_kafka_collection" "orders" {
    + description         = "Ingestion of sample data from Confluent Cloud."
    + field_mapping_query = <<-EOT
      SELECT
      COUNT(i.orderid) AS orders,
      SUM(i.orderunits) AS units,
      i.address.zipcode,
      i.address.state,
      -- bucket data in one hour buckets
      TIME_BUCKET(HOURS(1), TIMESTAMP_MILLIS(i.ordertime)) AS _event_time
      FROM
      _input AS i
      WHERE
      -- drop all records with an incorrect state
      i.address.state != 'State_'
      GROUP BY
      _event_time,
      i.address.zipcode,
      i.address.state
      -- CLUSTER BY
      -- 	state
      EOT
    + id                  = (known after apply)
    + insert_only         = true
    + name                = "orders"
    + retention_secs      = 3600
    + wait_for_collection = true
    + wait_for_documents  = 0
    + workspace           = "community"

    + source {
        + consumer_group_id   = (known after apply)
        + integration_name    = "confluent-cloud"
        + offset_reset_policy = "EARLIEST"
        + status              = (known after apply)
        + topic_name          = "test_json"
        + use_v3              = true
          }
          }

# rockset_kafka_integration.confluent will be created
+ resource "rockset_kafka_integration" "confluent" {
    + bootstrap_servers    = "pkc-pgq85.us-west-2.aws.confluent.cloud:9092"
    + connection_string    = (known after apply)
    + description          = "Integration to ingest documents from Confluent Cloud"
    + id                   = (known after apply)
    + name                 = "confluent-cloud"
    + security_config      = {
        + "api_key" = "5E6CVIXJRFSJY26J"
        + "secret"  = "WuPP0/aYRQbJyetBntjvGYbotOIRvBX9F4cETb3fmwS8Y3q38i9YUk1vYgcXFtWq"
          }
    + use_v3               = true
    + wait_for_integration = true
      }

# rockset_query_lambda.order-summary will be created
+ resource "rockset_query_lambda" "order-summary" {
    + description = "created by Rockset terraform provider"
    + id          = (known after apply)
    + name        = "orders-summary"
    + state       = (known after apply)
    + version     = (known after apply)
    + workspace   = "community"

    + sql {
        + query = <<-EOT
          SELECT
          count(orders) AS NumOrders,
          zipcode
          FROM
          community.production as o
          WHERE
          state = 'State_42' OR state = 'State_43'
          GROUP BY
          zipcode
          ORDER BY
          orders DESC
          EOT
          }
          }

# rockset_query_lambda_tag.production will be created
+ resource "rockset_query_lambda_tag" "production" {
    + id           = (known after apply)
    + name         = "production"
    + query_lambda = "orders-summary"
    + version      = "71cecbbf2d0a7cdc"
    + workspace    = "community"
      }

# rockset_role.query-only will be created
+ resource "rockset_role" "query-only" {
    + created_at  = (known after apply)
    + created_by  = (known after apply)
    + description = "This role can only query collections in the community workspace in the usw2a1 cluster"
    + id          = (known after apply)
    + name        = "query-only"
    + owner_email = (known after apply)

    + privilege {
        + action        = "EXECUTE_QUERY_LAMBDA_WS"
        + cluster       = "usw2a1"
        + resource_name = "community"
          }
    + privilege {
        + action        = "QUERY_DATA_WS"
        + cluster       = "usw2a1"
        + resource_name = "community"
          }
          }

# rockset_s3_collection.cities will be created
+ resource "rockset_s3_collection" "cities" {
    + description         = "This collection contains sample data from the Rockset public dataset from S3"
    + id                  = (known after apply)
    + insert_only         = false
    + name                = "cities"
    + wait_for_collection = true
    + wait_for_documents  = 0
    + workspace           = "community"

    + source {
        + bucket           = "rockset-public-datasets"
        + format           = "json"
        + integration_name = "rockset-public-collections"
        + pattern          = "cities/geonames-all-cities-with-a-population-1000.json"
          }
          }

# rockset_s3_integration.public will be created
+ resource "rockset_s3_integration" "public" {
    + aws_role_arn = "arn:aws:iam::469279130686:role/rockset-public-datasets"
    + description  = "Integration to access Rockset's public datasets"
    + id           = (known after apply)
    + name         = "rockset-public-collections"
      }

# rockset_view.state[0] will be created
+ resource "rockset_view" "state" {
    + created_by  = (known after apply)
    + description = "limit the view of the data to state_24"
    + id          = (known after apply)
    + name        = "state_24"
    + query       = <<-EOT
      SELECT
      *
      FROM
      community.production as o
      WHERE
      state = 'State_42'
      EOT
    + workspace   = "community"
      }

# rockset_view.state[1] will be created
+ resource "rockset_view" "state" {
    + created_by  = (known after apply)
    + description = "limit the view of the data to state_42"
    + id          = (known after apply)
    + name        = "state_42"
    + query       = <<-EOT
      SELECT
      *
      FROM
      community.production as o
      WHERE
      state = 'State_42'
      EOT
    + workspace   = "community"
      }

# rockset_workspace.community will be created
+ resource "rockset_workspace" "community" {
    + created_by  = (known after apply)
    + description = "created by Rockset terraform provider"
    + id          = (known after apply)
    + name        = "community"
      }

Plan: 12 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
Terraform will perform the actions described above.
Only 'yes' will be accepted to approve.

Enter a value:
```
</details>

## Updating

Now you can try to update e.g. the `states` variable, or the `orders-summary.sql.tftpl` and rerun `terraform apply`
to see how Rockset gets reconfigured with according to what you changed. 

```bash
$ terraform apply

...

Plan: 1 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value:
```

<details>
  <summary>Full terraform output</summary>

```
rockset_workspace.community: Refreshing state... [id=community]
rockset_s3_integration.public: Refreshing state... [id=rockset-public-collections]
rockset_kafka_integration.confluent: Refreshing state... [id=confluent-cloud]
rockset_role.query-only: Refreshing state... [id=query-only]
rockset_api_key.query-only: Refreshing state... [id=query-only]
rockset_s3_collection.cities: Refreshing state... [id=community.cities]
rockset_kafka_collection.orders: Refreshing state... [id=community.orders]
rockset_alias.production: Refreshing state... [id=community.production]
rockset_view.state[1]: Refreshing state... [id=community.state_42]
rockset_query_lambda.orders-summary: Refreshing state... [id=community.orders-summary]
rockset_view.state[0]: Refreshing state... [id=community.state_24]
rockset_query_lambda_tag.production: Refreshing state... [id=community.orders-summary.production]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
+ create
  ~ update in-place

Terraform will perform the following actions:

# rockset_query_lambda.orders-summary will be updated in-place
~ resource "rockset_query_lambda" "orders-summary" {
id          = "community.orders-summary"
name        = "orders-summary"
~ version     = "98aa5ebee6491386" -> (known after apply)
# (3 unchanged attributes hidden)

      + sql {
          + query = <<-EOT
                SELECT
                    count(orders) AS NumOrders,
                    zipcode
                FROM
                    community.production as o
                WHERE
                    state = 'state_24' OR state = 'state_42' OR state = 'state_49'
                GROUP BY
                    orders,
                    zipcode
                ORDER BY
                    orders DESC
            EOT
        }
      - sql {
          - query = <<-EOT
                SELECT
                    count(orders) AS NumOrders,
                    zipcode
                FROM
                    community.production as o
                WHERE
                    state = 'state_24' OR state = 'state_42'
                GROUP BY
                    orders,
                    zipcode
                ORDER BY
                    orders DESC
            EOT -> null
        }
    }

# rockset_view.state[2] will be created
+ resource "rockset_view" "state" {
    + created_by  = (known after apply)
    + description = "limit the view of the data to state_49"
    + id          = (known after apply)
    + name        = "state_49"
    + query       = <<-EOT
      SELECT
      *
      FROM
      community.production as o
      WHERE
      state = 'State_42'
      EOT
    + workspace   = "community"
      }

Plan: 1 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
Terraform will perform the actions described above.
Only 'yes' will be accepted to approve.

Enter a value:
```
</details>
