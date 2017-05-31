VERSION=$(sed -nE 's/ *__version__ *= *"([^"]+)".*/\1/p' ./{{cookiecutter.repo_name}}/__init__.py)

REGISTRY="{{cookiecutter.registry_name}}"
REPO="{{cookiecutter.repo_name}}"

install:
	python setup.py install

train:
	python -m dialogact $(train_data)

serve:
	python -m dialogact.app

build:
	docker build -t $REGISTRY/$REPO:latest .
	docker tag $REGISTRY/$REPO:latest $REGISTRY/$REPO:$VERSION

push:
	docker push $REGISTRY/$REPO:latest
	docker push $REGISTRY/$REPO:$VERSION
