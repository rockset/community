variable "bucket" {
  description = "Name of the S3 bucket to configure access for the Rockset S3 integration."
  type        = string
  default     = "rockset-community-datasets"
}

variable "bucket_prefix" {
  description = "S3 prefix for objects allowed to be accessed."
  type        = string
  default     = "*"
}

variable "rockset_role_name" {
  default     = "rockset-s3-integration"
  type        = string
  description = "Name of the AWS IAM role."
}

variable "retention_secs" {
  type        = number
  default     = 3600*24*30
  description = "Number of seconds to retain the documents (30 days)"
}

variable "stable_version" {
  type = string
  default = "0eb04bfed335946d"
  description = "Query Lambda version for the stable tag. If empty, the latest version is used."
}

variable "KAFKA_REST_ENDPOINT" {
  description = "Confluent Cloud bootstrap servers."
  type        = string
}

variable "KAFKA_API_KEY" {
  description = "Confluent Cloud API key."
  type        = string
}

variable "KAFKA_API_SECRET" {
  description = "Confluent Cloud secret."
  type        = string
}
