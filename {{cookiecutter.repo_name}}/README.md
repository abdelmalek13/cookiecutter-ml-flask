# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## Train the model

`python -m {{cookiecutter.repo_name}} train_data model_path [test_data]`

## Serve the model

To start the project on debug on port 8080, run `python -m {{cookiecutter.repo_name}}.app`

## Docker

Build the docker image with `./build_docker.sh`
