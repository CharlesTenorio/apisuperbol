up:
	sudo docker-compose up

bash:
	sudo docker-compose exec django bash

shell:
	sudo docker-compose exec django python manage.py shell

db-up:
	sudo docker-compose exec django python manage.py makemigrations
	sudo docker-compose exec django python manage.py migrate

reset-makemigrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete

lint:
	sudo docker-compose exec django flake8 --exit-zero --count --ignore E501,E111,E114,E121,E731,W503,W504 $(find . -path "*.py")

createsuperuser:
	sudo docker-compose exec django python manage.py createsuperuser

config:
	sudo docker-compose exec django python manage.py makemigrations
	sudo docker-compose exec django python manage.py migrate
	sudo docker-compose exec django python manage.py createsuperuser

stop:
	docker system prune

console:
	ssh deploy@186.237.57.210 -p2201