.PHONY: init clean update lint test format


init:
	python3.9 -m venv venv
	(source venv/bin/activate; pip install -e .)

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
