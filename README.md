# web-app
This is test app developed using python for testing a simple API call. And also demostrate the CI/CD process for deploying app on Kubernetes

## Overall setup
- This repo contains a simple python app with web API
- GitHub Actions CI/CD pipelines are created for generating docker container and test the container
- Once the container is tested, output will be displayed as a comment 
- CD pipline trigger upon commenting on PR with keyword `apply`
- CD pipline will push the docker container to the docker hub and
- Create Kubernetes resources in Azure Kubernetes cluster to deploy the python app
- If above steps are successful, PR will be automatically merged

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

## Usage
By user
1. Create a branch and modify the code as per your requirement. Example - change the json output of python script
2. Create a pull request

By admin
1. Review the pull request (updated code and comment section with terraform plan)
2. Approve PR if satisfied

By user
1. Once approved and all checks are passed, Add a comment `apply` in the PR
2. It will trigger the CD pipeline to deploy K8 resources and display the results
3. If terraform plan succeeds, it will merge the branch to master 
4. On the terraform output comment section, you can find the ingress IP 
5. Test the application using ingress ip
```
http://<ingress-ip>/hyphen/api/tasks
```

## Troubleshooting
Create another container in same AKS cluster to test the connectivity within same network
```
kubectl run -i --tty --rm debug --image=curlimages/curl:7.76.1 -- sh
```

## Azure Kubernetes Cluster
- This application is deployed on AKS
- AKS was created using Terraform code which you can find here - https://github.com/g1soori/terraform/tree/master/stage/aks-adv_network

## Pending
- Enable rolling updates for Kuberenetes deployment
