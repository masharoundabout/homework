import dataclasses
from enum import Enum


@dataclasses.dataclass()
class Hobbies(Enum):
    SPORT = 'Sports'
    READING = 'Reading'
    MUSIC = 'Music'