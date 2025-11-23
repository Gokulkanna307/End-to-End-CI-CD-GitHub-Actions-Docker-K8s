End-to-End CI/CD: GitHub Actions + Docker + Kubernetes
Objective

This project demonstrates a complete CI/CD pipeline that builds, tests, and deploys an application automatically using GitHub Actions, Docker, and a local Kubernetes cluster.

Overview

GitHub Actions is used to automate the pipeline.

Docker builds container images of the app.

Minikube or kind runs a local Kubernetes cluster to deploy the app.

Secrets are used for credentials securely.

Workflow Steps

Build & Test – GitHub Actions automatically builds the app and runs tests on every push.

Build Docker Image – A Docker image of the app is created.

Push Image – The image is pushed to Docker Hub (or a local registry if Docker Hub is unavailable).

Deploy to Kubernetes – Using kubectl and kubeconfig, the image is deployed to Minikube or kind.

Secrets Management – Credentials such as Docker Hub username/password are stored securely in GitHub Actions secrets.

Learning Outcome

Understand how CI/CD pipelines automate build, test, and deployment processes.

Learn to integrate GitHub Actions with Docker and Kubernetes.

Practice secure handling of credentials in pipelines.

Gain hands-on experience deploying applications locally in Kubernetes.
