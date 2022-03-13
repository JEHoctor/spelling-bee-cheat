import click

import spelling_bee


@click.command()
@click.option("-d", "--archive-dir",
              type=click.Path(exists=True, file_okay=False, writable=True, readable=True),
              default=spelling_bee.folders.PUZZLE_ARCHIVE_DIR)
def scrape(archive_dir: str):
    """
    Download today's and yesterday's spelling bee puzzles from the NYT website
    and save them in JSON files. The file names will contain the publication
    date. They will look like YYYY-MM-DD.json. You can control the archive
    directory with a flag, but the default is the puzzle_archive/ directory in
    the code repo.

    Args:
        archive_dir: folder in which to save the results
    """
    archive = spelling_bee.archive.Archive(archive_dir)
    tayp = archive.today_and_yesterday_puzzles()
    print("Archived", tayp.today.printDate)
    print("Archived", tayp.yesterday.printDate)


if __name__ == "__main__":
    scrape()
