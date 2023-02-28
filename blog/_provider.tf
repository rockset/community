terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4"
    }
    rockset = {
      source  = "rockset/rockset"
      version = "~> 0.6.2"
    }
  }

  backend "s3" {
    bucket = "rockset-community-terraform"
    key    = "blog/state"
    region = "us-west-2"
  }

  required_version = "~>1.3"
}

provider rockset {}

provider aws {
  region = "us-west-2"
}
