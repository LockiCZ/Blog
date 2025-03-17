migrate-make:
	python src/manage.py makemigrations

migrate: migrate-make
	python src/manage.py migrate

superuser:
	python src/manage.py createsuperuser

static:
	python src/manage.py collectstatic --noinput

build: static
	docker build --no-cache -t palmaf -t 0.1 .

asgi-start:
	cd src && uvicorn blog_site.asgi:application --reload --host 0.0.0.0 --port 8000

wsgi-start-prod:
	cd src && gunicorn blog_site.asgi:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 --workers 4 --threads 2 --log-level info

docker-start:
	docker-compose up -d --force-recreate

docker-stop:
	docker-compose down

# requires lang=xx
mkmsg:
	django-admin makemessages -l $(lang)
