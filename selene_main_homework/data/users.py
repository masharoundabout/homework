import dataclasses
from enum import Enum

@dataclasses.dataclass()
class Users:
    first_name: str
    last_name: str
    email: str
    gender: str
    telephone: str
    birthday_month: str
    birthday_year: str
    birthday_day: str
    subject: str
    picture: str
    hobby: Enum
    addr: str
    state: str
    city: str
