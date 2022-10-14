install:
	poetry install
lint:
	poetry run flake8 fizz_buzz
test:
	poetry run pytest
test-coverage:
	poetry run pytest --cov=fizz_buzz --cov-report xml tests/