export PYTHON_EXEC = python3.10
export NODE_VERSION = 16.17.0
export NPM_VERSION = 8.18.0
SHELL := /bin/bash
VENV="${CURDIR}/.venv"

venv:
	$(PYTHON_EXEC) -m venv .venv
	source $(VENV)/bin/activate && pip install -U pip nodeenv setuptools setuptools_scm wheel
	source $(VENV)/bin/activate && nodeenv -p -n $(NODE_VERSION)
	source $(VENV)/bin/activate && npm install -g npm@$(NPM_VERSION)
	source $(VENV)/bin/activate && npm install -g yarn
	source $(VENV)/bin/activate && cd backend && pip install -e .

docker_build:
	DOCKER_BUILDKIT=1 docker-compose build