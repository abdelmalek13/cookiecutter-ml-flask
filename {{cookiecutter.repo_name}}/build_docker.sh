#!/usr/bin/env bash

VERSION=$(sed -nE 's/ *__version__ *= *"([^"]+)".*/\1/p' ./{{cookiecutter.repo_name}}/{{cookiecutter.repo_name}}/__init__.py)

REGISTRY="{{cookiecutter.registry_name}}"
REPO="{{cookiecutter.repo_name}}"

docker build -t $REGISTRY/$REPO:latest .
docker tag $REGISTRY/$REPO:latest $REGISTRY/$REPO:$VERSION

# docker push $REGISTRY/$REPO:latest
# docker push $REGISTRY/$REPO:$VERSION
