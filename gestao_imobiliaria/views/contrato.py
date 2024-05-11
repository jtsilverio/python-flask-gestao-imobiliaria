from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from gestao_imobiliaria.db import get_db
from gestao_imobiliaria.views.utils import get_column_names, flash_errors
from gestao_imobiliaria.forms import ContratoForm

contrato = Blueprint("contrato", __name__)
PAGE_NAME = "contrato"


@contrato.route("/contrato/")
def contrato_list():
    PAGE_TITLE = PAGE_NAME
    db = get_db()
    colunas = get_column_names(db, table="contrato")

    dados = db.execute(
        """
        SELECT contrato.id, contrato.data_inicio, contrato.data_fim,
            contrato.valor_aluguel, contrato.IPTU, contrato.condominio,
            contrato.garantia, contrato.outras_despesas, contrato.porcentagem_comissao, 
            imovel.id||':'|| imovel.logradouro as id_imovel, 
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
        blueprint=PAGE_NAME,
    )


@contrato.route("/contrato/cadastro/")
def cadastro():
    PAGE_TITLE = "Cadastro Contrato"
    form = ContratoForm()
    db = get_db()

    if form.validate_on_submit():
        db.execute(
            """
            INSERT INTO contrato (data_inicio, data_fim, valor_aluguel, IPTU, condominio, 
                                  garantia, outras_despesas, porcentagem_comissao, 
                                  id_imovel, id_locatario) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                form.data_inicio.data,
                form.data_fim.data,
                form.valor_aluguel.data,
                form.IPTU.data,
                form.condominio.data,
                form.garantia.data,
                form.outras_despesas.data,
                form.porcentagem_comissao.data,
                form.id_imovel.data,
                form.id_locatario.data,
            ),
        )
        db.commit()
        flash("Cadastro Realizado com Sucesso.", "success")
        return redirect(url_for("contrato.contrato_list"))
    else:
        flash_errors(form)

    return render_template(
        "form.html",
        form=form,
        page_title=PAGE_TITLE,
    )


@contrato.route("/contrato/<int:id>", methods=["GET", "POST"])
def edit(id: int):
    db = get_db()
    form = ContratoForm()

    contrato = db.execute("SELECT * FROM contrato WHERE id = ?", (id,)).fetchone()
    if contrato is None:
        abort(404, "Contrato id {0} doesn't exist.".format(id))

    if request.method == "GET":
        form.data_inicio.data = contrato["data_inicio"]
        form.data_fim.data = contrato["data_fim"]
        form.valor_aluguel.data = contrato["valor_aluguel"]
        form.IPTU.data = contrato["IPTU"]
        form.condominio.data = contrato["condominio"]
        form.garantia.data = contrato["garantia"]
        form.outras_despesas.data = contrato["outras_despesas"]
        form.porcentagem_comissao.data = contrato["porcentagem_comissao"]
        form.id_imovel.data = contrato["id_imovel"]
        form.id_locatario.data = contrato["id_locatario"]

    if form.validate_on_submit():
        db.execute(
            """
            UPDATE contrato 
            SET data_inicio = ?,
                data_fim = ?,
                valor_aluguel = ?,
                IPTU = ?,
                condominio = ?,
                garantia = ?,
                outras_despesas = ?,
                porcentagem_comissao = ?,
                id_imovel = ?,
                id_locatario = ?
            WHERE id = ?
            """,
            (
                form.data_inicio.data,
                form.data_fim.data,
                form.valor_aluguel.data,
                form.IPTU.data,
                form.condominio.data,
                form.garantia.data,
                form.outras_despesas.data,
                form.porcentagem_comissao.data,
                form.id_imovel.data,
                form.id_locatario.data,
                id,
            ),
        )
        db.commit()
        flash("Contrato Atualizado com Sucesso.", "success")
        return redirect(url_for("contrato.contrato_list"))

    return render_template("form.html", form=form, page_title="Editar Contrato")


@contrato.route("/contrato/<int:id>/delete/", methods=["GET", "POST"])
def delete(id: int):
    db = get_db()
    db.execute("DELETE FROM contrato WHERE id = ?", (id,))
    db.commit()
    flash("Contrato deletado com sucesso.", "success")
    return redirect(url_for("contrato.contrato_list"))
