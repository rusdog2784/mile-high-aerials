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
# 		through terraform via github actions and vault. Oh, and here are some 
#		helpful links I was using:
#		- https://docs.github.com/en/actions/writing-workflows/quickstart
#		- https://www.freecodecamp.org/news/how-to-deploy-aws-infrastructure-with-terraform-and-github-actions-a-practical-multi-environment-ci-cd-guide/
#		- https://developer.hashicorp.com/terraform/tutorials/secrets/secrets-vault
#		- https://developer.hashicorp.com/vault/tutorials/getting-started/getting-started-deploy#initialize-vault
#		- https://developer.hashicorp.com/vault/docs/configuration
#		- https://developer.hashicorp.com/vault/tutorials/app-integration/github-actions#start-vault
#		- https://developer.hashicorp.com/terraform/tutorials/automation/github-actions#set-up-hcp-terraform