from pydantic import BaseModel
from typing import Optional


class Command(BaseModel):
    pass


class UserData(Command):  # Modelo de datos  que se van a guardar del alumno
    name: str
    age: Optional[int] = None
    age_in_months: Optional[float] = None


class FaceTestData(Command):  # Modelo de datos que van a almacenar las puntuaciones del primer test
    hits: int
    errors: int
    net_hits: int
    ici: int


class SpanTestData(Command):  # Modelo de datos que van a almacenar las puntuaciones del segundo test
    ri: int
