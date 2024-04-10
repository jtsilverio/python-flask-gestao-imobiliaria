PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PYTHON_INTERPRETER = python3

# Test if python is installed
ifeq (,$(shell $(PYTHON_INTERPRETER) --version))
$(error "Python is not installed!")
endif

.PHONY: clean
clean:
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete
	@find . -type d -name ".tox" -exec rm -r "{}" +
	@find . -type d -name ".pytest_cache" -exec rm -r "{}" +


install-pip-tools:
	$(PYTHON_INTERPRETER) -m pip install pip-tools


install-build:
	$(PYTHON_INTERPRETER) -m pip install build


pip-sync:
	pip-sync requirements.txt requirements-dev.txt

pip-compile: install-pip-tools install-build
	pip-compile --no-emit-index-url \
				--verbose \
				--generate-hashes \
				--output-file requirements.txt \
				--strip-extras \
				pyproject.toml

	pip-compile \
		-c requirements.txt \
		--verbose \
		--generate-hashes \
		--output-file requirements-dev.txt \
		--extra dev \
		pyproject.toml


requirements: pip-compile pip-sync
	echo "Requirements installed"

.PHONY: server
server:
	gunicorn --bind ":8888" -w 1 "main:create_app()"

docker-build:
	docker build -t gestao-imobiliaria .
