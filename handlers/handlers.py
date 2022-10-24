import pandas as pd

# from database.firebase import db
from domains.commands import UserData, TestData

TABLES = {
    'table_a': 'https://firebasestorage.googleapis.com/v0/b/prueba-tesis-8e65c.appspot.com/o/tabla1.csv?alt=media'
               '&token=7f02b523-7ea4-4d2d-b2ec-df05f4e8e083'
}


def calculate_face_test(user_data: UserData, test_data: TestData):
    df = pd.read_csv(TABLES.get('table_a'))
    print(df)
    return {
        "message": "ola"
    }


def test():
    # test = "D:\\tabla1.xlsx"
    df = pd.read_csv(TABLES.get('table_a'))
    # df = pd.read_excel(test)
    print(df)
    hit = 1
    # print(df['A'].where(df['A'] == hit))
    # print(df['A'])
    # print(type(df['A'][0]))


if __name__ == "__main__":
    test()
