init:
	cp .env.example .env

install:
	poetry install

run:
	poetry run python manage.py runserver

terminal:
	poetry run python manage.py shell

migrate:
	poetry run python manage.py migrate

makemigrate:
	poetry run python manage.py makemigrations

clean:
	rm -rf .venv __pycache__ .pytest_cache .coverage .mypy_cache db.sqlite3

.DEFAULT_GOAL := help

# Help command
help:
	@echo "Available targets:"
	@echo "  init        - Initialize the project"
	@echo "  install     - Install project dependencies"
	@echo "  run         - Run the Django application"
	@echo "  terminal    - Run the terminal in the virtual environment"
	@echo "  migrate     - Apply database migrations"
	@echo "  makemigrate - Create database migrations"
	@echo "  clean       - Clean up virtual environment and generated files"
	@echo "  help        - Show this help message"
	