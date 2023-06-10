start-dev:
	docker-compose --profile dev up --build

start-prod:
	docker-compose --profile prod up --build

.PHONY: start-dev start-prod
