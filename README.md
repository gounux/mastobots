# Mastobots - Various and diverse bots in the fediverse

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![flake8](https://img.shields.io/badge/linter-flake8-green)](https://flake8.pycqa.org/)

## Setup

`poetry` is used to manage environment and dependencies (python>=3.10)

Install poetry:

```bash
python -m pip install poetry
```

Install project's dependencies:

```bash
poetry install
```

Install pre-commit tools:

```bash
poetry run pre-commit install
```

## Configuration

The actionnable bots configuration is handled with a YAML file. `bot.config.example.yaml` is an example of such a bot config file.

Copy this config file, then you can edit it to fit your configuration:

```bash
cp bot.config.example.yaml bot.config.yaml
```



## Run

### Run using poetry CLI

```bash
poetry run python mastobots.py [POWER] bot.config.yaml
```

`POWER` refers to available bots, listed as keys in the config file

### Run using docker image

Create local docker image:

```bash
docker build -t mastobots:$(poetry version --short) -t mastobots:latest .
```

Run local docker image:

```bash
docker run mastobots:latest [POWER] bot.config.yaml
```
