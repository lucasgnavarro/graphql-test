.PHONY: build \
ingest-initial-data \
run-server \
test


.DEFAULT_GOAL := help

# FOR python requirements
VENV_FOLDER ?= .venv
REQUIREMENTS_FILE ?= dev-requirements.txt

help:
	@echo "    build"
	@echo "        Build docker image."
	@echo "    ingest-initial-data"
	@echo "        Ingest initial data for api."
	@echo "    test"
	@echo "        Run Tests"
	@echo "    run-server"
	@echo "        Start local web server"

build:
	@docker build . -t graphql-app

test:
	@docker-compose run graphql pytest --cov-report term --cov-report html --cov=app -s

run-server:
	@docker-compose up

ingest-initial-data:
	@docker-compose run graphql python manage.py migrate
	@docker-compose run graphql python manage.py ingest_admission_process --ignore_duplicated
	@docker-compose run graphql python manage.py ingest_students_csv /app/demo_data/student_records.csv
