# docker ########################################

build:
	@docker-compose build
	
up:
	@docker-compose up -d

migrate:
	@docker-compose exec app bash -c "./manage.py migrate"

superuser:
	@docker-compose exec app python manage.py shell --command \
	"from django.contrib.auth import get_user_model; \
	get_user_model().objects.create_superuser('user', 'user@admin.com', 'password')"
	@echo superuser created UN: user PW: password EM: user@admin.com

run:
	@docker-compose exec app bash -c "./manage.py runserver 0.0.0.0:8000"

down:
	@docker-compose down

destroy:
	@docker-compose down -v

sh:
	@docker-compose exec app bash

dbimport:
	@docker-compose exec db bash -c 'mysql -u user -ppassword app < /db_data/dump.sql'

collectstatic:
	@docker-compose exec app bash -c "./manage.py collectstatic --noinput"

env-vars:
	cp .env.example .env

# ansible ########################################

pull-db:
	@ansible-playbook ansible-pull-db.yml -i inventory

pull-media:
	@ansible-playbook ansible-pull-media.yml -i inventory

prod-deploy:
	@ansible-playbook ansible-production.yml -i inventory

# all
initial-all:
	@make build
	@make up
	@make migrate

# mail ########################################

mail:
	@echo "Starting mail server"
	@docker run -d -p 8025:8025 -p 1025:1025 --name mailhog mailhog/mailhog

mail-stop:
	@echo "Stopping mail server"
	@docker stop mailhog
	@docker rm mailhog
