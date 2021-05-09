# hyphen-app
This is test app developed using python for testing a simple API call. 

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