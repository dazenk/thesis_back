import pandas as pd

# from database.firebase import db
from domains.commands import UserData, TestData
from data.tables import TABLE_A

TABLES = {
    'table_a': 'https://firebasestorage.googleapis.com/v0/b/prueba-tesis-8e65c.appspot.com/o/tabla1.csv?alt=media'
               '&token=7f02b523-7ea4-4d2d-b2ec-df05f4e8e083'
}


def calculate_face_test(user_data: UserData, test_data: TestData):
    table_a = pd.DataFrame(TABLE_A)
    results = {
        "hits": int(search_value(df=table_a, column='A', value=test_data.hits)),
        "errors": int(search_value(df=table_a, column='E', value=test_data.errors)),
        "net_hits": int(search_value(df=table_a, column='A-E', value=test_data.net_hits)),
        "ici": int(search_value(df=table_a, column='ICI', value=test_data.ici))
    }
    return results


def search_value(df: pd.DataFrame, column: any, value: int):
    rows_quantity = len(df.index)
    for row_idx in range(rows_quantity):
        if type(df[column][row_idx]) == list:
            values_range = range(df[column][row_idx][0], df[column][row_idx][1])
            if value in values_range:
                return df['En'][row_idx]
        elif type(df[column][row_idx]) == int:
            if value == df[column][row_idx]:
                return df['En'][row_idx]
    return -1


def test():
    table_a = pd.DataFrame(TABLE_A)
    hits = 12
    errors = 7
    net_hits = 5
    ici = -10
    print(table_a)
    find_hit = search_value(df=table_a, column='ICI', value=ici)
    print(find_hit)


if __name__ == "__main__":
    test()
