# Hestia

## Introduction

Hestia is an implementation of the OpenAPI standard to the OMOP CDM and OHDSI tools.

## Features

- The OMOP CDM Schema in LinkML.
    - Easily transform the OMOP CDM into other frameworks, artefacts, and documentation.
- Offloading SQL translation and connectors to [Ibis](https://github.com/ibis-project/ibis)
- Composable API for OHDSI tooling using [OpenAPI v3.1.0](https://spec.openapis.org/oas/latest.html) standards.
- Decoupling of backend and frontend using [FastAPI](https://github.com/tiangolo/fastapi) and [FastUI](https://github.com/pydantic/FastUI).
- Human and Machine (e.g. [GPT with Actions](https://platform.openai.com/docs/actions/introduction)) readable API Documentation.


## Design


## Technology

| Name | Licence |
|------|---------|
| [FastAPI](https://fastapi.tiangolo.com/) | MIT |
| [Ibis](https://ibis-project.org/) | Apache License 2.0 |
| [Pydantic](https://docs.pydantic.dev/latest/) | MIT |
| [Duckdb](https://github.com/duckdb/duckdb) | MIT |
| [Pytest](https://github.com/pytest-dev/pytest) | MIT |
| [Ruff](https://github.com/astral-sh/ruff) | MIT |
| [Docker Engine](https://docs.docker.com/engine/) | Apache License 2.0 |
| [FastUI](https://github.com/pydantic/FastUI) | MIT|



## Installation

```bash
pip install ...
```

```bash
conda install ...
```

## Usage

## Documentation

[LinkLM Documentation](https://linkml.io/linkml/)

[OpenAPI Documentation](https://spec.openapis.org/oas/latest.html)

## Support



## Development
### Development Status
Pre-alpha 



## Contributing

- Please read our [CONTRIBUTING.md](.github/CONTRIBUTING.md) document.


## References

- [zhanymkanov/fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices?tab=readme-ov-file#project-structure)
- [tiangolo/full-stack-fastapi-template](https://github.com/tiangolo/full-stack-fastapi-template)

## License
Hestia is licensed under [Apache License 2.0](./LICENSE)