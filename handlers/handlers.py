import pandas as pd

# from database.firebase import db
from domains.commands import UserData, TestData
from data.tables import TABLE_A, TABLE_B, TABLE_C, TABLE_D, TABLE_E, TABLE_F, TABLE_G

TABLES = {
    6: TABLE_A,
    7: TABLE_A,
    8: TABLE_B,
    9: TABLE_C,
    10: TABLE_D,
    11: TABLE_E,
    12: TABLE_F,
    13: TABLE_G
}


def calculate_face_test(user_data: UserData, test_data: TestData):
    table = pd.DataFrame(TABLES.get(user_data.age))
    results = {
        "hits": search_value(df=table, column='A', value=test_data.hits),
        "errors": search_value(df=table, column='E', value=test_data.errors),
        "net_hits": search_value(df=table, column='A-E', value=test_data.net_hits),
        "ici": search_value(df=table, column='ICI', value=test_data.ici)
    }
    return results


def search_value(df: pd.DataFrame, column: any, value: int):
    rows_quantity = len(df.index)
    found_value = -1
    for row_idx in range(rows_quantity):
        if type(df[column][row_idx]) == list:
            values_range = range(df[column][row_idx][0], df[column][row_idx][1]+1)
            if value in values_range:
                found_value = df['En'][row_idx]
        elif type(df[column][row_idx]) == int:
            if value == df[column][row_idx]:
                found_value = df['En'][row_idx]
    return int(found_value)


if __name__ == "__main__":
    age = 13
    table_tes = pd.DataFrame(TABLES.get(age))
