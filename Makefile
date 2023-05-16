.PHONY: init clean update lint test format scrape


init:
	python3.11 -m venv venv
	(source venv/bin/activate; pip install -e .)
	(source venv/bin/activate; pip install -r dev-requirements.txt)

clean:
	rm -rf venv/

update: clean init

lint:
	ruff spelling_bee_cheat/ tests/ scripts/

test: lint
	pytest -vv tests/spelling_bee_cheat

format:
	black spelling_bee_cheat/ tests/ scripts/
	isort spelling_bee_cheat/ tests/ scripts/

scrape:
	(source venv/bin/activate; scrape.py)
