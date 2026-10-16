# Container and Terraform experiments: reviewer guide

Application services and Docker Compose configurations alongside Terraform infrastructure directories.

## Start the review

Explain which Compose stack and Terraform root you actually use. A source tree alone does not establish the old README's deployment and free-tier claims.

| Source | Review focus |\n| --- | --- |\n| [docker-compose.yml](docker-compose.yml) | Build context, runtime configuration, ports, and persistence |\n| [terraform/environments/dev/devops-keys.pemls](terraform/environments/dev/devops-keys.pemls) | Inputs, state, permissions, cost, and resource lifecycle |\n| [terraform/environments/dev/main.tf](terraform/environments/dev/main.tf) | Inputs, state, permissions, cost, and resource lifecycle |\n| [terraform/environments/dev/terraform.tfvars.example](terraform/environments/dev/terraform.tfvars.example) | Inputs, state, permissions, cost, and resource lifecycle |\n| [terraform/environments/dev/variables.tf](terraform/environments/dev/variables.tf) | Inputs, state, permissions, cost, and resource lifecycle |\n| [terraform/main.tf](terraform/main.tf) | Inputs, state, permissions, cost, and resource lifecycle |

## A useful interview walkthrough

1. State the problem and the specific part you implemented or changed.
2. Open the source above and follow one request, release, or failure from start to finish.
3. Show a reproducible result, including an actual failure and the observation that confirms recovery.
4. Explain one tradeoff and one limitation. Distinguish a local test from a live deployment.

## Evidence and limits

This guide is based on the default-branch source inspected on 16 October 2026. It is a source review, not a fresh deployment or a certification of every feature. Existing CI runs and tests should be checked at the commit being demonstrated. Do not present screenshots, inherited code, planned features, or old README statements as proof of a current deployment.
