# 🚀 Automated CI/CD Pipeline with Infrastructure Provisioning using Terraform on AWS

## Project Overview
This project demonstrates a complete DevOps workflow with:
- **Infrastructure as Code** using Terraform
- **CI/CD pipeline** using GitHub Actions
- **Containerized microservices** (Node.js, Python)
- **Automated deployment** to AWS EC2
- **Container Registry** using AWS ECR

## 🎯 Project Status: **COMPLETED & DEPLOYED** ✅

The infrastructure is fully deployed and running on AWS Free Tier with:
- EC2 instance running Docker containers
- API Gateway and User Service microservices
- ECR repository for container images
- VPC with public subnets and security groups

## Architecture

┌─────────────────────────────────────────────────────────────┐
│ GitHub Actions CI/CD │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│ │ Test │→│ Scan │→│ Build │→│ Push │ │
│ └──────────┘ └──────────┘ └──────────┘ └──────────┘ │
└─────────────────────────────────────────────────────────────┘
↓
┌─────────────────────────────────────────────────────────────┐
│ AWS Cloud │
│ ┌────────────────────────────────────────────────────┐ │
│ │ Terraform Provisioned Infrastructure │ │
│ │ • VPC with Public Subnets (10.0.1.0/24) │ │
│ │ • EC2 (t3.micro) with Docker │ │
│ │ • ECR Container Registry │ │
│ │ • IAM Roles (Least Privilege) │ │
│ └────────────────────────────────────────────────────┘ │
│ ↓ │
│ ┌────────────────────────────────────────────────────┐ │
│ │ Microservices (Docker Compose) │ │
│ │ • API Gateway (Node.js) - Port 80 │ │
│ │ • User Service (Python) - Port 8000 │ │
│ └────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘

## Technology Stack

| Category | Technologies |
|----------|--------------|
| **Infrastructure** | Terraform, AWS (VPC, EC2, ECR, IAM) |
| **CI/CD** | GitHub Actions, Docker |
| **Backend** | Node.js, Python (FastAPI) |
| **Container** | Docker, Docker Compose |
| **Security** | IAM Least Privilege |

## Prerequisites

- AWS Account (Free Tier)
- Terraform >= 1.0
- Docker >= 20.10
- GitHub Account
- AWS CLI configured

## Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/Vishnu063/My_Project.git
cd My_Project

2. Configure AWS credentials
aws configure
# Enter your AWS Access Key ID and Secret Access Key
# Default region: us-east-1

3. Deploy infrastructure with Terraform

bash
cd terraform/environments/dev
terraform init
terraform plan
terraform apply -auto-approve
4. Build and push Docker images to ECR

bash
cd ../../../app

# Build API Gateway
cd api-gateway
docker build -t api-gateway:latest .
docker tag api-gateway:latest 138300868541.dkr.ecr.us-east-1.amazonaws.com/devops-cicd-dev:api-gateway-latest
docker push 138300868541.dkr.ecr.us-east-1.amazonaws.com/devops-cicd-dev:api-gateway-latest
cd ..

# Build User Service
cd user-service
docker build -t user-service:latest .
docker tag user-service:latest 138300868541.dkr.ecr.us-east-1.amazonaws.com/devops-cicd-dev:user-service-latest
docker push 138300868541.dkr.ecr.us-east-1.amazonaws.com/devops-cicd-dev:user-service-latest
cd ..
5. Deploy to EC2

bash
# Get EC2 public IP
EC2_IP=$(cd ../terraform/environments/dev && terraform output -raw ec2_public_ip)

# SSH into EC2 and deploy
ssh -i devops-key-new.pem ubuntu@$EC2_IP << 'EOF'
cd ~/app
docker compose pull
docker compose up -d
curl localhost/health
EOF
6. Test the live API

bash
# Health check
curl http://$EC2_IP/health

# API information
curl http://$EC2_IP/api/info

# List users
curl http://$EC2_IP/api/users

# Create a new user
curl -X POST http://$EC2_IP/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"New User","email":"new@example.com"}'
