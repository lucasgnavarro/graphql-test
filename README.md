# Small showcase project.
A small project using django models + graphql

# Disclaimer
- I would love to make some dataloader to perform a demo around that but unable due to time.
- the project it's very tiny but i use a couple of hours of my free time, the idea was to show a database interaction with graphene + basic testing suite, if its required, i can make the proper mutations + subscriptions based on what we require to evaluate.
- if it's required I can make it all async
- if it's required I can add postgresq configuration in docker-compose and switch from sqlite to PG
- testing suite is not complete but the idea is to make a small showcase using factories + graphene Client.
- i'll make a single commit due to time but i use to make commits using conventions as https://www.conventionalcommits.org/en/v1.0.0/.

## Pre-requirements
- Python >= 3.8
- Docker
- docker-compose

### Structure
```
├── Dockerfile
├── Makefile
├── README.md
├── apps
│ ├── admission # Admissions folder, i've tried to mimic enrollwise admission graphql query
│ │             # i've got metadata from https://www.chooseousd.org/graphql/ introspection query
│ ├── core
│ │      ├── schema.py # General schema
│ └── students
│── config               # CONFIG folder
│── demo_data
│── docker-compose.yml
├── manage.py
├── pytest.ini
└── requirements.txt
```

### Each module / app has
- models.py -> django models definition
- schema.py -> GraphQL schema definition
- test folder, test suite.

`apps.core.schema` centralize the schemas (inherits from `AdmissionProcessesQuery`, `StudentsQuery`)



# Available commands:
Run `make` in root folder
- build: Build docker image.
- ingest-initial-data: Ingest initial data for api.
- test: Run Tests.
- run-server: Start local web server.


## Recommended path
- make build
- make ingest-initial-data
- make run-server
