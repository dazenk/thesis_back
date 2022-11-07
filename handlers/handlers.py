import pandas as pd
import json
# from database.firebase import db
from domains.commands import UserData, FaceTestData, SpanTestData
from data.tables import TABLE_A_FT, TABLE_B_FT, TABLE_C_FT, TABLE_D_FT, TABLE_E_FT, TABLE_F_FT, TABLE_G_FT, TABLE_A_ST, \
    TABLE_B_ST, TABLE_C_ST, TABLE_D_ST, TABLE_E_ST, TABLE_F_ST, TABLE_G_ST, TABLE_H_ST, TABLE_I_ST, TABLE_J_ST, \
    TABLE_K_ST, TABLE_L_ST, TABLE_M_ST, TABLE_N_ST, TABLE_O_ST, TABLE_P_ST, TABLE_Q_ST, TABLE_R_ST, TABLE_S_ST, \
    TABLE_T_ST, TABLE_U_ST, TABLE_V_ST


TABLES_FT = {
    6: TABLE_A_FT,
    7: TABLE_A_FT,
    8: TABLE_B_FT,
    9: TABLE_C_FT,
    10: TABLE_D_FT,
    11: TABLE_E_FT,
    12: TABLE_F_FT,
    13: TABLE_G_FT
}

TABLES_ST = {
    0: TABLE_A_ST,
    1: TABLE_B_ST,
    2: TABLE_C_ST,
    3: TABLE_D_ST,
    4: TABLE_E_ST,
    5: TABLE_F_ST,
    6: TABLE_G_ST,
    7: TABLE_H_ST,
    8: TABLE_I_ST,
    9: TABLE_J_ST,
    10: TABLE_K_ST,
    11: TABLE_L_ST,
    12: TABLE_M_ST,
    13: TABLE_N_ST,
    14: TABLE_O_ST,
    15: TABLE_P_ST,
    16: TABLE_Q_ST,
    17: TABLE_R_ST,
    18: TABLE_S_ST,
    19: TABLE_T_ST,
    20: TABLE_U_ST,
    21: TABLE_V_ST
}

AGE_RANGES = [
    (72, 78),
    (79, 84),
    (85, 90),
    (91, 96),
    (97, 102),
    (103, 108),
    (109, 114),
    (115, 120),
    (121, 126),
    (127, 132),
    (133, 138),
    (139, 144),
    (145, 150),
    (151, 156),
    (157, 162),
    (163, 168),
    (169, 174),
    (175, 180),
    (181, 186),
    (187, 192),
    (193, 198),
    (199, 204)
]


def calculate_face_test(user_data: UserData, test_data: FaceTestData):
    table = pd.DataFrame(TABLES_FT.get(user_data.age))
    results = {
        "hits": search_value(df=table, column='A', value=test_data.hits, result_column='En'),
        "errors": search_value(df=table, column='E', value=test_data.errors, result_column='En'),
        "net_hits": search_value(df=table, column='A-E', value=test_data.net_hits, result_column='En'),
        "ici": search_value(df=table, column='ICI', value=test_data.ici, result_column='En')
    }
    return results


def search_value(df: pd.DataFrame, column: any, value: int, result_column: any):
    rows_quantity = len(df.index)
    found_value = -1
    for row_idx in range(rows_quantity):
        if type(df[column][row_idx]) == list:
            values_range = range(df[column][row_idx][0], df[column][row_idx][1]+1)
            if value in values_range:
                found_value = df[result_column][row_idx]
        elif type(df[column][row_idx]) == int:
            if value == df[column][row_idx]:
                found_value = df[result_column][row_idx]
    return int(found_value)


def calculate_span_test(user_data: UserData, test_data: SpanTestData):
    result = None
    table_idx = search_age_range(age=user_data.age_in_months)
    if table_idx != -1:
        table = pd.DataFrame(TABLES_ST.get(table_idx))
        result = {
            "RE": search_value(df=table, column='RI', value=test_data.ri, result_column='PE')
        }
    return result


def search_age_range(age: float):
    pos = -1
    for idx in range(len(AGE_RANGES)):
        if AGE_RANGES[idx][0] <= age <= AGE_RANGES[idx][1]:
            pos = idx
    return pos


if __name__ == "__main__":
    url = 'https://firebasestorage.googleapis.com/v0/b/prueba-tesis-8e65c.appspot.com/o/tabla22-span.csv?alt=media&token=c4749a7a-54db-4682-b128-389882a21777'
    df = pd.read_csv(url)
    dic = df.to_dict(orient='records')
    json_dic = json.dumps(dic, indent=4)
    print(json_dic)
