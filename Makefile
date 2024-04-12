.ONESHELL:
SHELL=/bin/bash
.PHONY: build

config ?= .env

include $(config)
export $(shell sed 's/=.*//' $(config))

GIT_COMMIT := $(shell git rev-parse --short HEAD)

all: lock build-image run-local

lock:
	@echo 'Creating poetry lockfile'
	poetry lock

build-image:
	@echo 'Building release ${CONTAINER_REGISTRY}/analytics/$(IMAGE_NAME):$(IMAGE_TAG)'
# build your image
	docker compose -f docker-compose-build.yaml build --build-arg SOURCE_COMMIT=$(GIT_COMMIT) app

push-registry:
# login into our azure registry
	az acr login -n lgvudh
# push image to the registry
	docker push  ${CONTAINER_REGISTRY}/analytics/$(IMAGE_NAME):$(IMAGE_TAG)

install:
	copy .env.example .env
	mamba env create -f environment.yaml -p ./.venv
	mamba activate ./.venv
	poetry install

run-local:
	pygeoapi serve --flask

run-local-container:
# run container in foreground
	docker compose -f docker-compose-dev.yaml up

build-docs:
	jupyter-book build docs

clean-docs:
	jupyter-book clean docs

