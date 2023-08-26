## environment setup

- python: 3.10.10
- mysql: 8.0
- django

## init project

- run cmd: python -m django startproject django_project
- cd folder django_project: cd django_project
- init app: python manage.py startapp django_app

## run project

- install package: python -m pip install -r requirement.txt
- run migrate: python manage.py migrate
- start project: python manage.py runserver
## create supperuser
- run cmd: python manage.py createsuperuser --username=admin --email=vodinhnghia85@gmail.com
## link project

- link home page: http://localhost:8000
- link admin: http://localhost:8000/admin
