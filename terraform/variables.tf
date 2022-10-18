variable "production_version" {
  description = "Query lambda version used for the production tag. If left blank the latest version of the query lambda is used."
  default = "71cecbbf2d0a7cdc"
}

variable "KAFKA_REST_ENDPOINT" {
  description = "Confluent Cloud bootstrap servers."
  type = string
}

variable "KAFKA_API_KEY" {
  description = "Confluent Cloud API key."
  type = string
}

variable "KAFKA_API_SECRET" {
  description = "Confluent Cloud secret."
  type = string
}
