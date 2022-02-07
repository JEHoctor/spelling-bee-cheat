import typing as tp

from pydantic import BaseModel


class Puzzle(BaseModel):
    """
    Representation of the JSON puzzle data used by NYT.
    """

    expiration: int
    displayWeekday: str
    displayDate: str
    printDate: str
    centerLetter: str
    outerLetters: tp.List[str]
    validLetters: tp.List[str]
    pangrams: tp.List[str]
    answers: tp.List[str]
    id: int
    freeExpiration: int
    editor: str
