PIP := venv/bin/pip
PYTHON3 := venv/bin/python3

clear:
	rm -rf venv

venv:
	python3 -m venv venv

install_requirements:
	${PIP} install -r requirements.txt

run:
	${PYTHON3} content/manage.py runserver

create_migrations:
	${PYTHON3} content/manage.py makemigrations

migrations:
	${PYTHON3} content/manage.py migrate

up_service:
	make clear
	make venv
	make install_requirements
	make migrations
	make run

superuser:
	${PYTHON3} content/manage.py createsuperuser
