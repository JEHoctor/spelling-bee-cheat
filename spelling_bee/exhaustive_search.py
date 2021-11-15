from itertools import product
from typing import List

def exhaustive_search(
    letters: str,
    center_letter: str,
    length: int,
) -> List[str]:
    """
    Args:
        letters:
        center_letter:
        length:

    Returns:
        List[str]: a list of character strings that obey the rules of the game
    """
    words_found: List[str] = []
    for letters in product(*[letters]*length):
        if center_letter in letters:
            words_found.append("".join(letters))
    return words_found
