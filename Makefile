build:
	- docker compose build --no-cache

dev:
	- ./bin/odoo start -i base -d odoo