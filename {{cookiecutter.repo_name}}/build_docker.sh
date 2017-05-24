#!/usr/bin/env bash

VERSION=0.1.0

REGISTRY="{{cookiecutter.registry_name}}"
REPO="{{cookiecutter.repo_name}}"

docker build -t $REGISTRY/$REPO:latest .
docker tag $REGISTRY/$REPO:latest $REGISTRY/$REPO:$VERSION

# docker push $REGISTRY/$REPO:latest
# docker push $REGISTRY/$REPO:$VERSION
