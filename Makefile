install:
	cd app && pipenv install

dev-install:
	cd app && \
	pipenv install --dev && \
	pipenv run pre-commit install --hook-type pre-commit --hook-type pre-push

up:
	docker compose up -d

down:
	docker compose down

test-coverage: postgres-up
	cd app && pipenv run coverage erase
	rm -rf app/htmlcov
	cd app && pipenv run coverage run -m pytest
	cd app && pipenv run coverage html

postgres-up:
	docker compose up postgres -d
