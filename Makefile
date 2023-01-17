dev:
		docker-compose up

dev-down:
		docker-compose down

make exec:
		docker exec -it odoo16_learn_web bash

make update_app:
		-c /home/dev/odoo16/config/odoo.conf -d odoo16_learn -u om_hospital