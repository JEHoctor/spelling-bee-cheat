.PHONY: init clean update lint test format scrape package package-upload


init:
	python3.12 -m venv venv
	(source venv/bin/activate; pip install -e .[dev])
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

package:
	(source venv/bin/activate; python3 -m build)

package-upload:
	(source venv/bin/activate; python3 -m twine upload dist/*)
