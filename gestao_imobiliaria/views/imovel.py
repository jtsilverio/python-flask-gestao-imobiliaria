from flask import current_app, render_template

from gestao_imobiliaria.db import get_db
from gestao_imobiliaria.views.utils import get_column_names


@current_app.route("/imovel/")
def imoveis_list():
    PAGE_TITLE = "imovel"
    db = get_db()
    colunas = get_column_names(db, table="imovel")

    dados = db.execute(
        """
        SELECT imovel.id, endereco_logradouro, endereco_numero, endereco_complemento, 
        endereco_bairro, endereco_cidade, endereco_estado, 
        endereco_cep, alugado, locador.id||':'|| locador.primeiro_nome as id_locador
        FROM imovel
        INNER JOIN locador ON imovel.id_locador = locador.id;
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
