import json
import re
import requests
from dataclasses import

from bs4 import BeautifulSoup

PUZZLE_URL = "https://www.nytimes.com/puzzles/spelling-bee"

def daily_hint_url(year: int, month: int, day: int) -> str:
    return f"https://www.nytimes.com/{year}/{month}/{day}/crosswords/spelling-bee-forum.html"

def fetch_puzzle_data():
    r = requests.get(PUZZLE_URL)
    soup = BeautifulSoup(r.text, "html.parser")
    scripts = soup.find_all("script")
    for script in scripts:
        if window.gameData

@dataclass
class PuzzleData:
    """
    Class representing a spelling bee puzzle
    """

    def __init__(
        self,
        print_date: str,
    ):
        """
        Initializer for PuzzleData

        Args:
            print_date: date string
        """
