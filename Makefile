.PHONY:
.ONESHELL:

include .env
export

datahub-up:
	poetry run datahub docker quickstart --quickstart-compose-file ./compose-datahub.yaml

datahub-down:
	poetry run datahub docker quickstart --stop

oltp-dwh-up:
	docker compose -f ./compose-postgres.yaml up -d

down:
	docker compose -f ./compose-postgres.yaml down && docker volume remove hm-scalablerecs_recsys-dwh
	poetry run datahub docker quickstart --stop