.PHONY: init clean update lint test format scrape


init:
	python3.11 -m venv venv
	(source venv/bin/activate; pip install -e .)
	(source venv/bin/activate; pip install -r dev-requirements.txt)

clean:
	rm -rf venv/

update: clean init

lint:
	flake8 spelling_bee/ tests/ scripts/

test: lint
	pytest -vv tests/spelling_bee

format:
	black spelling_bee/ tests/ scripts/
	isort spelling_bee/ tests/ scripts/

scrape:
	(source venv/bin/activate; scrape.py)
