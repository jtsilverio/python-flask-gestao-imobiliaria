from functools import cache


@cache
def get_column_names(db, table):
    cursor = db.execute(f"PRAGMA table_info({table})")
    colunas = [column[1] for column in cursor.fetchall()]

    for i in range(len(colunas)):
        colunas[i] = colunas[i].replace("id_", "")
        colunas[i] = colunas[i].replace("_", " ")
        colunas[i] = colunas[i].upper()

    return colunas
