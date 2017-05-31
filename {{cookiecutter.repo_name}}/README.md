# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## Train the model

`python -m {{cookiecutter.repo_name}} <train_data> <model_path> [test_data]` or `make train_data=<train_data> train`

## Serve the model

To start the project on debug on port 8080, run `python -m {{cookiecutter.repo_name}}.app` or `make serve`

## Docker

Build the docker image typing `make build` and push it to the registry with `make push`
