from pydantic import BaseModel
from typing import Optional


class Command(BaseModel):
    pass


class UserData(Command):
    name: str
    age: Optional[int] = None
    age_in_months: Optional[float] = None


class FaceTestData(Command):
    hits: int
    errors: int
    net_hits: int
    ici: int


class SpanTestData(Command):
    ri: int
