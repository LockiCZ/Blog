migrate-make:
	python palmaf/manage.py makemigrations

migrate:
	python palmaf/manage.py migrate

static:
	python palmaf/manage.py collectstatic --noinput

build: static
	docker build --no-cache -t palmaf -t 0.1 .

asgi-start:
	cd palmaf && uvicorn my_site.asgi:application --reload --host 0.0.0.0 --port 8000

wsgi-start-prod:
	cd palmaf && gunicorn my_site.asgi:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 --workers 4 --threads 2 --log-level info

docker-start:
	docker-compose up -d --force-recreate

docker-stop:
	docker-compose down