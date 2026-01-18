#!/bin/sh
kubectl apply -f namespace.yaml
kubectl apply -f configmap.yaml -n django
kubectl apply -f secret.yaml -n django
kubectl apply -f deployment.yaml -n django
kubectl apply -f service.yaml -n django
