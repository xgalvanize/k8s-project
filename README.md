# k8s-project
## Secrets

Secrets are not committed to the repository.

To run locally or in Kubernetes:

```bash
cp kubernetes/secret.example.yaml kubernetes/secret.yaml
kubectl apply -f kubernetes/secret.yaml
