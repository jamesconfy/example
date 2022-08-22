setup:
	python3 -m venv venv
	source venv/bin/activate

remove:
	deactivate

install:
	pip install --upgrade pip && pip install -r requirements.txt

migrations:
	flask db init
	flask db migrate -m "First migrate"
	flask db upgrade
	flask db stamp head

run:
	gunicorn --bind 0.0.0.0:808 run:app