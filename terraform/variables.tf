variable "states" {
  description = "States to generate views for"
  type = list(string)
  default = ["state_24", "state_42", "state_49"]
}

variable "production_version" {
  description = "Query lambda version used for the production tag. If left blank the latest version of the query lambda is used."
  default = "6c7451cc23bdc1b8"
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
