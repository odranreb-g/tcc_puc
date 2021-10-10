# Project

## KubeCtl

### Instalation

https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

## Kind - K8S - Cluster

### Instalation

The (link)[https://kind.sigs.k8s.io/docs/user/quick-start#installation] to install.

The following code has a path to /usr/local/bin you should change this to local present in your path.

```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.11.1/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

### Create Cluster

```bash
kind create cluster --config=./kind/kindconfig.yaml
``` 

### Install Contour Ingress

```bash
kubectl apply -f ./kind/contour.yaml

kubectl patch daemonsets -n projectcontour envoy -p '{"spec":{"template":{"spec":{"nodeSelector":{"ingress-ready":"true"},"tolerations":[{"key":"node-role.kubernetes.io/master","operator":"Equal","effect":"NoSchedule"}]}}}}'

```

## K8S

### How to conect to the pod

kubectl exec --stdin --tty <pod-name> -- /bin/bash

## GraphModels

### How to use

Add follow code to Dockerfile

```bash
RUN apt-get update \
    && apt-get install -y --no-install-recommends graphviz \
    && rm -rf /var/lib/apt/lists/* \
    && poetry add pyparsing pydot
```

### How to conect to docker?

```bash
docker run --network host -it --entrypoint=bash deliveries_api:0.0.1
```

### How to generate?

1. Enter into container

```bash

```

2. Type the command

```bash
./<api>/manage.py graph_models -g -X TimeStampedModel -o my_project_visualized.png
```

### How to copy from container?

```bash
docker cp b278c7bffe49:/app/my_project_visualized.png
```
