terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.62.0"
    }
  }
}

provider "aws" {
    region = "us-east-2"
}

# TODO: Left off looking into terraform, github actions, and terraform's vault
# 		provider. My end goal is to get this service deployed to AWS using 
#		terraform. Then any updates and changes to the service will be done 
# 		through terraform via github actions and vault.