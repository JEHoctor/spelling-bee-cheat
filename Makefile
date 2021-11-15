.PHONY: init lint test format


init:
	python -m venv venv
	(source venv/bin/activate; pip install -e .)

lint:
	flake8 spelling_bee

test: lint
	pytest -vv tests/spelling_bee

format:
	black spelling_bee
