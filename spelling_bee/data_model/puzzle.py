import typing as tp

from pydantic import BaseModel


class Puzzle(BaseModel):
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
