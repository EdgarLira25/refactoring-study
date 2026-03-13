from datetime import datetime
from typing import NamedTuple


class Person(NamedTuple):
    name: str


class Photo(NamedTuple):
    title: str
    date: datetime
    location: str


class Stream:
    def __init__(self) -> None:
        self.text = ""

    def write(self, text: str):
        self.text += text
