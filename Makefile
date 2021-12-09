.PHONY: init clean update lint test format scrape


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

scrape:
	(source venv/bin/activate; scrape.py -d puzzle_archive/)
