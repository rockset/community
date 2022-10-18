terraform {
  cloud {
    organization = "rockset-community"

    workspaces {
      name = "community"
    }
  }

  required_providers {
    rockset = {
      source  = "rockset/rockset"
      version = "~>0.6"
    }
    confluent = {
      source  = "confluentinc/confluent"
      version = "~>1.7"
    }
  }
  required_version = "~>1.3"
}
