import dataclasses
from enum import EnumDict

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
    hobby: EnumDict
    addr: str
    state: str
    city: str