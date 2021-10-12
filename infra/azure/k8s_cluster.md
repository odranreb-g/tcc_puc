#

##

### Azure resource group

az group create --name tccPucBernardoGomes --location eastus

### Azure Container Registry

az acr create --resource-group tccPucBernardoGomes --name tccPucBernardoGomes --sku Basic

### Log in to the container registry

az acr login --name tccPucBernardoGomes

### ACR list acrloginserver

az acr list --resource-group tccpucbernardogomes --query "[].{acrLoginServer:loginServer}" --output table

### TAG images

docker tag mcr.microsoft.com/azuredocs/azure-vote-front:v1 <acrLoginServer>/azure-vote-front:v1

docker tag tcc_deliveries_api:0.0.6 tccpucbernardogomes.azurecr.io/tcc_deliveries_api:0.0.6
### PUSH IMages

docker push <acrLoginServer>/azure-vote-front:v1

docker push tccpucbernardogomes.azurecr.io/tcc_deliveries_api:0.0.6

### List image in container

az acr repository list --name tccpucbernardogomes --output table

### See tags 

az acr repository show-tags --name tccpucbernardogomes --repository azure-vote-front --output table

### Create K8S Cluster

The keys SSH key files id_rsa and id_rsa.pub will be replaced.

az aks create \
    --resource-group tccpucbernardogomes \
    --name tccPucBernardoAKSCluster \
    --node-count 2 \
    --generate-ssh-keys \
    --attach-acr tccpucbernardogomes


### Connect to cluster using kubectl

az aks get-credentials --resource-group tccpucbernardogomes --name tccPucBernardoAKSCluster

### Test cluster

kubectl get nodes