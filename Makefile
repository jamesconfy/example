setup:
	python3 -m venv venv

activate:
	source .venv/bin/activate

deactivate:
	deactivate

install:
	pip install --upgrade pip && pip install -r requirements.txt

migrations:
	flask db init
	flask db migrate -m "First migrate"
	flask db upgrade
	flask db stamp head

lint:
	hadolint --ignore=DL3042 --ignore=DL3013 Dockerfile
	pylint --disable=R,C,W1203,W1202 run.py

run:
	gunicorn --bind 0.0.0.0:808 run:app