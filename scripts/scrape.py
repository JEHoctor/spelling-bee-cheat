import pickle
from pathlib import Path

import click

import spelling_bee


@click.command()
def scrape():
    pdat = spelling_bee.PuzzleData.fetch_today()
    dest = Path() / f"puzzle_{pdat.date}.pkl"
    with dest.open("wb") as f:
        pickle.dump(pdat, f)


if __name__ == "__main__":
    scrape()
