# README: Python Monitoring Application using Flask and Docker on EKS

This README will guide you through creating a Python monitoring application using Flask and Docker, containerizing it, and deploying it to EKS cluster. We will cover the following steps:

How to create Python Monitoring Application using Flask from scratch.
How to run the Python application locally on port 5000
How to containerize the application using Docker
How to write Dockerfile
How to build Docker image from Dockerfile
How to run Docker container from Docker image
How to create ECR and push image to the Repo
How to create EKS cluster and nodes
How to create Kubernetes Deployments and service using Python
How to port forward and expose the Kubernetes application

## Step 1: Creating Python Monitoring Application using Flask

To create a Python monitoring application using Flask, you need to have Python and Flask installed on your local machine. You can create a basic Flask application by following the Flask documentation or by using any available Flask boilerplate. Once you have created the application, you can test it by running it locally on port 5000.

## Step 2: Running the Python application locally on port 5000

To run the Python application locally on port 5000, you need to navigate to the root directory of your Flask application and execute the following command:

'python app.py'

This will start your Flask application on port 5000, and you can access it using your web browser.

## Step 3: Containerizing the application using Docker

To containerize the Python application, you need to create a Dockerfile. The Dockerfile is a set of instructions that tell Docker how to build your application. We will cover this in the next step.

## Step 4: Writing Dockerfile

The Dockerfile contains instructions for building the Docker image. It defines the base image, the application code to be copied, and the commands to be executed. You can create a Dockerfile by following the Docker documentation or by using any available Docker boilerplate.

## Step 5: Building Docker image from Dockerfile

To build a Docker image from the Dockerfile, navigate to the directory containing the Dockerfile and execute the following command:

'docker build -t my-image-name .'

This will build a Docker image with the specified name.

## Step 6: Running Docker container from Docker image

To run a Docker container from the Docker image, execute the following command:

'docker run -p 5000:5000 my-image-name'

> This will start a Docker container and map port 5000 of the container to port 5000 of  your local machine. You can access the Flask application by navigating to [localhost](http://localhost:5000) in your web browser.

## Step 7: Creating ECR and pushing image to the Repo

To create an ECR repository and push the Docker image to it, you need to have an AWS account and AWS CLI installed. You can create an ECR repository using the AWS console or the AWS CLI. Once the repository is created, you can push the Docker image to it using the following commands:

```bash
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account_id>.dkr.ecr.<region>.amazonaws.com
docker tag my-image-name <account_id>.dkr.ecr.<region>.amazonaws.com/my-repo-name:my-tag
docker push <account_id>.dkr.ecr.<region>.amazonaws.com/my-repo-name:my-tag 
```

## Step 8: Creating EKS cluster and nodes

To create an EKS cluster and nodes, you need to have an AWS account and AWS CLI installed. You can create an EKS cluster using the AWS console or the AWS CLI. Once the cluster is created, you can create a node group to run your Docker containers. The node group is a set of EC2 instances that run your containers. You can create a node group using the following command:

```bash
eksctl create nodegroup --cluster <cluster_name> --name <node_group_name> --instance-types <instance_types> --node-labels "nodegroup=<node_group_name>" --node-ami <node_ami_id> --nodes <number_of_nodes> --asg-access
```

## Step 9: Creating Kubernetes Deployments and service using Python

To create Kubernetes Deployments and service using Python, you need to have kubectl and AWS CLI installed. You can use the Kubernetes Python client to create Deployments and services. The client provides a simple interface for interacting with Kubernetes resources. You can create a Deployment and service using the following code:

```python
from kubernetes import client, config

config.load_kube_config()
api = client.CoreV1Api()

# Create a deployment
deployment = client.V1Deployment(...)
api.create_namespaced_deployment(namespace="default", body=deployment)

# Create a service
service = client.V1Service(...)
api.create_namespaced_service(namespace="default", body=service)

```

## Step 10: Port forwarding and exposing the Kubernetes application

To access the Kubernetes application, you need to port forward the service to your local machine. You can use the following command to port forward the service:

```bash
kubectl port-forward service/<service_name> <local_port>:<service_port>
```

> This will forward the service port to your local port. You can access the Kubernetes application by navigating to [localhost](http://localhost:5000) in your web browser.

To expose the Kubernetes application to the internet, you can create an ingress resource. The ingress resource defines the rules for routing traffic to your service. You can create an ingress resource using the following code:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
spec:
  rules:
  - host: my-domain.com
    http:
      paths:
      - path: /my-path
        pathType: Prefix
        backend:
          service:
            name: my-service
            port:
              name: http
```

>This will create an ingress resource that routes traffic to your service based on the specified rules.
