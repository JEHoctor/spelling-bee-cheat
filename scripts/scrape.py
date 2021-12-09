import pickle
from pathlib import Path

import click

import spelling_bee


@click.command()
@click.option("-d", "--dest", type=click.Path(exists=True))
def scrape(dest: str):
    """
    Download today's spelling bee puzzle from the NYT website and save it in a
    pickle file. The file name will contain today's date in the file name. It
    will look like puzzle_YYYY-MM-DD.pkl. You can control the destination
    directory with a flag.

    Args:
        dest: folder in which to save the result
    """
    pdat = spelling_bee.PuzzleData.fetch_today()
    dest_path = Path(dest) / f"puzzle_{pdat.date}.pkl"
    if dest_path.exists():
        raise RuntimeError("File already exists: {dest_path}")
    with dest_path.open("wb") as f:
        pickle.dump(pdat, f)


if __name__ == "__main__":
    scrape()
