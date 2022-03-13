from pathlib import Path

from spelling_bee.data_model.puzzle import Puzzle
from spelling_bee.folders import PUZZLE_ARCHIVE_DIR
from spelling_bee.scrape.scrape import TodayAndYesterdayPuzzles


Pathlike = str | Path

class Archive:
    """
    Class to manage an archive of old spelling bee puzzles.
    """

    def __init__(self, path: Pathlike = PUZZLE_ARCHIVE_DIR):
        """
        Initializer for Archive class

        Args:
            path: directory in which to archive puzzles
        """
        self.path = Path(path)
        self.path.mkdir(parents=True, exist_ok=True)

    def path_from_iso8601(self, date_iso8601: str) -> Path:
        """
        Return the storage location for a puzzle from the puzzle date.

        Args:
            date_iso8601: a date string like "2022-02-26"
        """
        return self.path / f"{date_iso8601}.json"

    def puzzle_from_iso8601(self, date_iso8601: str) -> Puzzle | None:
        """
        Look for an archived puzzle from the requested date. Return None if not
        found. Expects date to be formatted according to ISO 8601.

        Args:
            date_iso8601: a date string like "2022-02-26"
        """
        in_path = self.path_from_iso8601(date_iso8601)
        if not in_path.exists():
            return None
        with in_path.open("r") as f:
            return Puzzle.parse_raw(f.read())

    def archive(self, puzzle: Puzzle) -> None:
        """
        Save a Puzzle in the directory as JSON. Choose a file name from the
        publication date of the puzzle.

        Args:
            puzzle: puzzle to save
        """
        out_path = self.path_from_iso8601(puzzle.printDate)
        with out_path.open("w") as f:
            f.write(puzzle.json())

    def today_and_yesterday_puzzles(self) -> TodayAndYesterdayPuzzles:
        """
        Fetch and archive the puzzles from today and yesterday.

        Returns:
            TodayAndYesterdayPuzzles: object containing both puzzles
        """
        tayp = TodayAndYesterdayPuzzles.fetch()
        self.archive(tayp.today)
        self.archive(tayp.yesterday)
        return tayp

    def today_puzzle(self) -> Puzzle:
        """
        Fetch and archive the puzzles from today and yesterday, returning only
        today's puzzle.

        Returns:
            Puzzle: today's puzzle
        """
        tayp = self.today_and_yesterday_puzzles()
        return tayp.today

    def yesterday_puzzle(self) -> Puzzle:
        """
        Fetch and archive the puzzles from today and yesterday, returning only
        yesterday's puzzle.

        Returns:
            Puzzle: yesterday's puzzle
        """
        tayp = self.today_and_yesterday_puzzles()
        return tayp.yesterday
