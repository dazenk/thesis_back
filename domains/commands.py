from pydantic import BaseModel


class Command(BaseModel):
    pass


class UserData(Command):
    name: str
    age: int


class TestData(Command):
    hits: int
    errors: int
    net_hits: int
    ici: int
