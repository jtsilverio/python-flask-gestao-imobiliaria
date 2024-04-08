from flask import current_app, render_template

from gestao_imobiliaria.db import get_db
from gestao_imobiliaria.views.utils import get_column_names


@current_app.route("/locatario/")
def locatario_list():
    PAGE_TITLE = "locatario"
    db = get_db()
    colunas = get_column_names(db, table="locatario")

    dados = db.execute(
        """
        SELECT id, primeiro_nome, ultimo_nome, email, ddd, telefone, tipo_logradouro, endereco, numero, cep
        FROM locatario;
        """
    ).fetchall()

    if dados is None:
        dados = []

    return render_template(
        "list.html",
        dados=dados,
        colunas=colunas,
        page_title=PAGE_TITLE,
    )