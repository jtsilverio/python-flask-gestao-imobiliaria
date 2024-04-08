from functools import cache

from flask import flash


@cache
def get_column_names(db, table):
    cursor = db.execute(f"PRAGMA table_info({table})")
    colunas = [column[1] for column in cursor.fetchall()]

    for i in range(len(colunas)):
        colunas[i] = colunas[i].replace("id_", "")
        colunas[i] = colunas[i].replace("_", " ")
        colunas[i] = colunas[i].upper()

    return colunas


def flash_errors(form):
    """Flashes form errors"""
    error_msgs = []
    for field, errors in form.errors.items():
        for error in errors:
            error_msgs.append(f"Erro: {getattr(form, field).label.text} - {error}")
    if len(error_msgs) > 0:
        flash(
            error_msgs,  # noqa
            "danger",
        )
