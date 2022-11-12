run:
	python -m morning_bot

lint:
	black .
	isort .

req:
	poetry export -f requirements.txt --without-hashes --with dev --output requirements.txt
