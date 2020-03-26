# Code repository for flask based portfolio website

What is this repository for -

- [Flask application]
- [Docker commands]
- [Kubernetes Commands]


## Creating a docker system from scratch

```shell
login to https://www.katacoda.com/courses/ubuntu/playground

$ docker run -it ubuntu:latest bash
```

=====================================================================

## How to run this website

```shell
$ git clone https://github.com/arunksingh16/python_website.git

$ docker build -t flask-sample:v1 .

$ docker build --file Dockerfile_2 -t flask-sample:v1

$ docker run -d -p 5000:5000 flask-sample:v1
```

## How to connect the running container and look for logs

```shell
$ docker exec -it <container_id> /bin/bash

$ docker logs <container_id>
```

## Checking in these images in hub

```shell
$ docker build . -t arun161087/flask-portfolio:v1

$ docker push arun161087/flask-portfolio:v1
```

## Other Support commands

```shell
$ docker inspect
$ docker history <img name>
$ docker ps
$ docker stop
$ docker 
```


=====================================================================

# Kubernetes Experiment

```shell
$ kubectl run pod1 --image=arun161087/flask-portfolio:v1 --generator=run-pod/v1 --dry-run
$ kubectl run pod1 --image=arun161087/flask-portfolio:v1 --generator=run-pod/v1
$ kubectl get pods -o wide
$ kubectl label pods pod1 env=dev

# pod operation

$ kubectl get pods 
$ kubectl get pods -o wide 
$ kubectl describe pod 
$ kubectl get pods -o wide --show-labels --all-namespaces 
$ kubectl delete pods


# Support Commands

$ kubectl get nodes
$ kubectl describe nodes
$ kubectl get namespace
$ kubectl get pods --all-namespaces




```