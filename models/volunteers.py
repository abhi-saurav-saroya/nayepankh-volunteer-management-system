from dataclasses import dataclass


@dataclass
class Volunteer:
    id: int | None
    name: str
    age: int
    gender: str
    phone: str
    email: str
    city: str
    skill: str
    availability: str
    join_date: str