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
