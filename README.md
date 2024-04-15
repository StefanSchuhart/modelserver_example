# Project description
This is an example pygeoapi server with plugins for the deployment of ogc api processes.

## Run the application
First, clone this project.

To run the application execute:

```bash
# running for the first time:
make install
```

```bash
# every time the service has stopped or must be restartet
make run-local
```
## Hello World example process usage

```bash
curl -XPOST http://localhost:5000/processes/hello-world/execution?f=js
on -d '{"inputs": {"name":"Me", "message": "Hi there"}}' -H "Content-Type: application/json"
```


## Developing a pygeoapi plugin and registering it with pygeoapi

* create a folder inside [src/example_ogcapi_processes](src/example_ogcapi_processes), e.g.: `my_cool_process`
* create an `__init__.py` file inside that folder
* create one or more python files that contains the logic of your process
* create a class that inherits from `pygeoapi.process.base.BaseProcessor`
* that class should parse dict/json as input parameters
* add a `PROCESS_METADATA` variable of type `dict` that contains process metadata and describes input and output parameters
    * example: [src/example_ogcapi_processes/sqrt_processor.process.py](src/example_ogcapi_processes/sqrt_processor.process.py)
* install the package or update the installation
* add an entry to `pygeoapi-config.yml` under `resources`:

```yaml
resources:
  squareroot:
    # name may refer to an external Python class, that is loaded by pygeoapi at runtime
    processor:
        name: example_ogcapi_processes.sqrt_processor.process.SlowSqrtProcessor
    type: process
```

## using processes
When entering `make run-local` on the commandline, an openapi document is created based on `pygeoapi-config.yml`.

Browse to http://localhost:5000/openapi and try out your process.

## Using the templating engine copier

Updating the underlying copier project template:

```bash
copier update . --trust
```

## General project content description

### Folders and files

**Folders**:

- `assets`: images
- `data`: local data
- `reports`: interactive reports
- `examples`: should contain working usage examples for this project
- `scratch`: personal or shared code snippets, trials, experiments, must not work
- `secrets`: contains passwords/secrets
- `scripts`: contains bash scripts automating some tasks used for this project
- `src`: contains actual code as plugins for pygeoapi server
- `.vscode`: settings and debug configurations

**Files**:
- Build management
    * `Makefile`: build project

- Container/image management:
    * `Dockerfile`: project container image definition
    * `docker-compose-build.yaml` : image build configuration
    * `docker-compose-dev.yaml`: container definition for development purposes
    * `docker-compose.yaml`: container definition for production usage

- virtual environments for this project:
    * `environment.yaml`: project virtual python environment

- `.env.example`: example, contains environment variable definitions for this project, copy it to `.env`
- `.gitignore`: contains files to ignore from source control
- `.dockerignore`: contains files to ignore by the docker daemon
- `pyproject.toml`: plugin requirements
- `poetry.lock`:

### manual environment management
- `mamba/conda`: create/manage virtual environments
- `poetry`: use to install all project/module requirements

```bash
# create a venv
mamba create -p ./.venv -f environment.yaml
```

```bash
# activate venv
conda activate .venv/
```

```bash
# update existing venv
mamba env update --prefix ./.venv --file environment.yaml  --prune
```

### How To use poetry to install dependencies

Add a package to your depdendency list (updates pyproject.toml) and install it in your environment
```bash
# add a dependency and install it, with
poetry add PACKAGE
```

```bash
# install your package in editable mode, into your environment
poetry install
```
