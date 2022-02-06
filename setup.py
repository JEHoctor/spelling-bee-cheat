from setuptools import setup

setup(
    name="spelling_bee",
    version="0.0.1",
    packages=["spelling_bee"],
    install_requires=[
        "black",
        "beautifulsoup4",
        "click",
        "flake8",
        "isort",
        "jupyter",
        "more-itertools",
        "nltk",
        "numpy",
        "pandas",
        "pytest",
        "scikit-learn",
        "seaborn",
        "spacy",
        "transformers",
    ],
    scripts=[
        "scripts/markov.py",
        "scripts/scrape.py",
    ],
)
