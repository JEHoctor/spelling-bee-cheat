from setuptools import setup

setup(
    name="spelling_bee",
    version="0.0.1",
    packages=["spelling_bee"],
    install_requires=[
        "black",
        "flake8",
        "jupyter",
        "nltk",
        "numpy",
        "pandas",
        "pytest",
        "scikit-learn",
        "seaborn",
        "spacy",
        "transformers",
    ],
)