from flask import current_app, render_template

from gestao_imobiliaria.db import get_db
from gestao_imobiliaria.views.utils import get_column_names


@current_app.route("/contrato/")
def contrato_list():
    PAGE_TITLE = "contrato"
    db = get_db()
    colunas = get_column_names(db, table="contrato")

    dados = db.execute(
        """
        SELECT contrato.id, contrato.data_inicio, contrato.data_fim,
            contrato.valor_aluguel, contrato.IPTU, contrato.condominio,
            contrato.garantia, contrato.outras_despesas, contrato.porcentagem_comissao, 
            imovel.id||':'|| imovel.endereco_logradouro as id_imovel, 
            locatario.id||':'|| locatario.primeiro_nome as id_locatario
        FROM contrato 
        INNER JOIN imovel ON contrato.id_imovel = imovel.id
        INNER JOIN locatario ON contrato.id_locatario = locatario.id
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
