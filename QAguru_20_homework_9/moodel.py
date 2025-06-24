from dataclasses import dataclass
from enum import Enum


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class Hobby(Enum):
    SPORTS = "Sports"
    MUSIC = "Music"
    READING = "Reading"


class State (Enum):
    NCR = "NCR"
    UTTAR_PRADESH = "Utar Pradesh"
    HARYANA = "Haryana"
    RAJASTHAN = "Rajasthan"


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile: str
    birthday: str
    subject: str
    hobby: Hobby
    picture_name: str
    adress:str
    state: State
    city: str
