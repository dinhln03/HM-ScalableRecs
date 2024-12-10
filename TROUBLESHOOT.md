# Troubleshooting
Records the bugs/issues occurring throught the project.

## Poetry install hangs
Possible cause:
- Python KEYRING issue. Likely this happens on Ubuntu.

Possible Solution:
- Run `export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring` before `poetry install`

## Poetry doesn't use your virtual environment created in the project
Possible cause:
- The config for virtual environments is not set up correctly.

Possible Solution:
- Run `poetry config virtualenvs.create true && poetry config virtualenvs.in-project true`

## Dependency failed to start: container datahub-mysql is unhealthy
Possible cause:
-  The old SQL volume cannot be reused.

Possible Solution:

1. Make sure to make down the datahub and delete the datahub-mysql and datahub-mysql-setup first
```sh
make datahub-down
docker rm -f `<datahub-mysql-container-id>`
docker rm -f `<datahub-mysql-setup-container-id>`
```

2. Remove the old SQL volume
```sh
docker volume rm datahub_mysqldata
```

## Cannot install psycopg2
Possible cause:
- Havent figured out yet

Possible Solution:
- Run `apt install libpq-dev gcc` and then run `poetry add psycopg2 && poetry install` 
