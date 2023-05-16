.PHONY: init clean update lint test format scrape


init:
	python3.11 -m venv venv
	(source venv/bin/activate; pip install -e .)
	(source venv/bin/activate; pip install -r dev-requirements.txt)

clean:
	rm -rf venv/

update: clean init

lint:
	ruff src/spelling_bee_cheat/ tests/

test: lint
	pytest -vv tests/spelling_bee_cheat

format:
	black src/spelling_bee_cheat/ tests/
	isort src/spelling_bee_cheat/ tests/

scrape:
	mkdir -p puzzle_archive/
	(source venv/bin/activate; scrape --archive-dir="puzzle_archive/")
