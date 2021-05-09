# hyphen-app
This is test app developed using python for testing a simple API call. 

## Overall setup
- This repo contains a simple python app with web API
- GitHub Actions CI/CD pipelines are created for generating docker containera= and test the container
- Once the container is tested, output will be displayed as a comment 
- CD pipline trigger upon merging the PR
- CD pipline will push the docker container to the docker hub and
- Create Kubernetes resources in Azure Kubernetes cluster to deploy the python app

## List of files included in main folder
- hyphen-app.py - Python script
- Dockerfile - Build the docker image using docker file
- requirements.tx - dependencies required for python
- main.yml - GitHub Actions workflow file

## k8s folder
- Terraform code for creating K8s resources
- Resources includes deployment, cluster service and ingress 

## k8s-yml
Contains k8s yaml files for reference but not in use

## Troubleshooting
Create another container in same AKS cluster to test the connectivity within same network
```
kubectl run -i --tty --rm debug --image=curlimages/curl:7.76.1 -- sh
```

## Azure Kubernetes Cluster
- This application is deployed on AKS
- AKS was created using Terraform code which you can find here - https://github.com/g1soori/terraform/tree/master/stage/aks-adv_network

## Pending
- Create Azure application GW to route external traffic to ingress resource