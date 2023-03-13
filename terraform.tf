terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.28.0"
    }
  }
  required_version = ">= 1.0.0"

  # backend "remote" {
  #   hostname     = "app.terraform.io"
  #   organization = var.tf_cloud_organization

  #   workspaces {
  #     name = var.workspace_name
  #   }
  # }
}
