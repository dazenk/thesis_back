# from database.firebase import db
from domains.commands import UserData, TestData

TABLE_A = {
    "PC": [],
    "A": [],
    "E": [],
    "A-E": [],
    "ICI": [],
    "En": []
}


def calculate_face_test(user_data: UserData, test_data: TestData):
    return {
        "message": "ola"
    }
