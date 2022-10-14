install:
	poetry install
lint:
	poetry run flake8 fizz_buzz
test:
	poetry run pytest