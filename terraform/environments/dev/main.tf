terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# Network Module
module "network" {
  source = "../../modules/network"
  
  project_name           = var.project_name
  environment            = var.environment
  vpc_cidr               = var.vpc_cidr
  public_subnet_cidrs    = var.public_subnet_cidrs
  availability_zones     = var.availability_zones
}

# Compute Module
module "compute" {
  source = "../../modules/compute"
  
  project_name       = var.project_name
  environment        = var.environment
  instance_type      = var.instance_type
  subnet_id          = module.network.public_subnet_ids[0]
  security_group_id  = module.network.security_group_id
  key_name           = var.key_name
}

# ECR Repository
resource "aws_ecr_repository" "app" {
  name = "${var.project_name}-${var.environment}"
  
  image_scanning_configuration {
    scan_on_push = true
  }
  
  image_tag_mutability = "MUTABLE"
  
  encryption_configuration {
    encryption_type = "AES256"
  }
  
  tags = {
    Name        = "${var.project_name}-ecr"
    Environment = var.environment
    Project     = var.project_name
  }
}

# S3 Bucket for Application Assets (optional)
resource "aws_s3_bucket" "app_assets" {
  bucket = "${var.project_name}-assets-${var.environment}-${random_id.bucket_suffix.hex}"
  
  tags = {
    Name        = "${var.project_name}-assets"
    Environment = var.environment
  }
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}

# Outputs
output "ec2_public_ip" {
  value = module.compute.public_ip
  description = "Public IP of the EC2 instance"
}

output "ec2_private_ip" {
  value = module.compute.private_ip
  description = "Private IP of the EC2 instance"
}

output "ecr_repository_url" {
  value = aws_ecr_repository.app.repository_url
  description = "URL of the ECR repository"
}

output "vpc_id" {
  value = module.network.vpc_id
  description = "VPC ID"
}

output "security_group_id" {
  value = module.network.security_group_id
  description = "Security Group ID"
}
