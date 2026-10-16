# Container and Terraform Experiments

A collection of application and infrastructure experiments, including a Node.js API gateway, Python user services, a Go product service, Docker Compose, and AWS Terraform configuration.

[Reviewer walkthrough](INTERVIEW.md)

## Choose the correct source tree

| Path | Contents |
| --- | --- |
| [app](app) | API gateway, user/product services, and nested Compose stack |
| [docker-compose.yml](docker-compose.yml) | Separate root Compose configuration |
| [flask-user](flask-user) | Standalone Python service experiment |
| [terraform](terraform) | Root, module, environment, and remote-state material |

There are multiple entry points. Inspect the specific Compose file and Terraform root before running commands; do not assume they describe one finished deployment.

## Review without provisioning

```bash
git clone https://github.com/Vishnu063/My_Project.git
cd My_Project
docker compose -f docker-compose.yml config --quiet
docker compose -f app/docker-compose.yml config --quiet
```

Configuration checks need Docker Compose and may require local environment values. They do not start services or prove runtime health, and were not executed in this portfolio pass.

The earlier README described a completed live deployment and free-tier operation. This source review does not establish either. Before using this as a primary interview demo, select one stack, verify it end to end, and document the exact commands and observed results. Review tracked Terraform plan/backup artifacts for environment-specific information; never commit state or private credentials.
