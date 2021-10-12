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
kind create cluster --config=./infra/kind/kindconfig.yaml
```

### Install Contour Ingress

```bash
kubectl apply -f ./kind/contour.yaml

kubectl patch daemonsets -n projectcontour envoy -p '{"spec":{"template":{"spec":{"nodeSelector":{"ingress-ready":"true"},"tolerations":[{"key":"node-role.kubernetes.io/master","operator":"Equal","effect":"NoSchedule"}]}}}}'

```

### Kind build and load images

cd projects/deliveries_api && \
 docker build . -t tcc_deliveries_api:0.0.6 && \
 kind load docker-image tcc_deliveries_api:0.0.6 && \
 cd -

cd projects/partner_routes_api && \
docker build . -t tcc_partner_routes_api:0.0.5 && \
kind load docker-image tcc_partner_routes_api:0.0.5 && \
cd -

cd projects/legacy_system && \
 docker build . -t tcc_legacy_system:0.0.4 && \
 kind load docker-image tcc_legacy_system:0.0.4 && \
 cd -

cd projects/pooling_system && \
docker build . -t tcc_pooling_system:0.0.3 && \
kind load docker-image tcc_pooling_system:0.0.3 && \
cd -

cd projects/new_partner_routes_service && \
docker build . -t tcc_new_partner_routes_service:0.0.1 && \
kind load docker-image tcc_new_partner_routes_service:0.0.1 && \
cd -

cd projects/pool_partner_price_service && \
docker build . -t tcc_pool_partner_price_service:0.0.1 && \
kind load docker-image tcc_pool_partner_price_service:0.0.1 && \
cd -

cd projects/zpl_generate_service && \
docker build . -t tcc_zpl_generate_service:0.0.1 && \
kind load docker-image tcc_zpl_generate_service:0.0.1 && \
cd -

### Migrate databases

kubectl exec --stdin --tty pod/partner-routes-api-76d6ff669c-7gwnj -- partner_routes_api/manage.py migrate
kubectl exec --stdin --tty pod/deliveries-api-69fcfcf487-5jtdz -- deliveries_api/manage.py migrate
kubectl exec --stdin --tty pod/legacy-system-67cbf489db-c6zzq -- legacy/manage.py migrate

### SCRIPTS

kubectl exec --stdin --tty $(kubectl get pods --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}' -l app=legacy-system) -- legacy/manage.py create_partner_routes

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
