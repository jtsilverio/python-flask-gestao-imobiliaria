from functools import cache

from flask import current_app, render_template

from gestao_imobiliaria.db import get_db


@cache
def get_column_names(db, table):
    cursor = db.execute(f"PRAGMA table_info({table})")
    colunas = [column[1] for column in cursor.fetchall()]

    for i in range(len(colunas)):
        colunas[i] = colunas[i].replace("id_", "")
        colunas[i] = colunas[i].replace("_", " ")
        colunas[i] = colunas[i].upper()

    return colunas


@current_app.route("/")
def index():
    PAGE_TITLE = "home"
    return render_template("home.html", page_title=PAGE_TITLE)


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


@current_app.route("/locador/")
def locador_list():
    PAGE_TITLE = "locador"
    db = get_db()
    colunas = get_column_names(db, table="locador")

    dados = db.execute(
        """
        SELECT id, primeiro_nome, ultimo_nome, email, ddd, telefone, tipo_logradouro, endereco, numero, cep
        FROM locador;
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
