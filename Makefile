install:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

train:
	python -m src.models.train --config configs/default.yaml

test:
	pytest -q

lint:
	flake8 src tests
