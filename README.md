# k8s-project

## 🧠 Overview

This project demonstrates deploying a Django app to Kubernetes
using a local Minikube cluster.

It includes:
- Dockerfile and docker-compose for containerization
- Kubernetes manifests
- Documentation for secrets

## Secrets

Secrets are not committed to the repository.

To run locally or in Kubernetes:

```bash
cp kubernetes/secret.example.yaml kubernetes/secret.yaml
kubectl apply -f kubernetes/secret.yaml
