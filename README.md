# Automated CI/CD Pipeline with Infrastructure Provisioning using Terraform on AWS

## Project Overview
This project demonstrates a complete DevOps workflow with:
- Infrastructure as Code using Terraform
- CI/CD pipeline using GitHub Actions
- Containerized microservices
- Automated deployment to AWS

## Prerequisites
- AWS Account (Free Tier)
- Terraform
- Docker
- GitHub Account

## Project Structure
├── .github/workflows/ # CI/CD pipeline definitions
├── terraform/ # Infrastructure as Code
├── app/ # Application code
├── scripts/ # Helper scripts
└── docs/ # Documentation
.
├── .github/workflows/ # CI/CD pipeline definitions
├── terraform/ # Infrastructure as Code
│ ├── modules/ # Reusable Terraform modules
│ │ ├── network/ # VPC, subnets, security groups
│ │ ├── compute/ # EC2 instances, IAM roles
│ │ └── security/ # Security configurations
│ ├── environments/ # Environment-specific configs
│ │ ├── dev/ # Development environment
│ │ └── prod/ # Production environment
│ └── remote-state/ # S3 backend configuration
├── app/ # Application code
│ ├── api-gateway/ # Node.js API gateway
│ ├── user-service/ # Python user service
│ └── product-service/ # Go product service
├── scripts/ # Helper scripts
└── docs/ # Documentation

## Deployment Status
🚧 Under Construction 🚧
