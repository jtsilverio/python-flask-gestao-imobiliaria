from flask import Blueprint, abort, flash, redirect, render_template, request, url_for

from gestao_imobiliaria.db import get_db
from gestao_imobiliaria.forms import ImovelForm
from gestao_imobiliaria.views.utils import flash_errors, get_column_names

imovel = Blueprint("imovel", __name__)
PAGE_NAME = "imovel"


@imovel.route("/imovel/")
def imovel_list():
    PAGE_TITLE = "imovel"
    db = get_db()
    colunas = get_column_names(db, table="imovel")

    dados = db.execute(
        """
        SELECT imovel.id, imovel.cep, imovel.logradouro, imovel.numero, imovel.complemento, 
        imovel.bairro, imovel.cidade, imovel.uf, 
        imovel.alugado, locador.id||':'|| locador.primeiro_nome as id_locador
        FROM imovel
        INNER JOIN locador ON imovel.id_locador = locador.id
        ORDER BY imovel.id DESC;
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


@imovel.route("/imovel/cadastro/", methods=["GET", "POST"])
def cadastro():
    PAGE_TITLE = "Cadastro Imovel"
    form = ImovelForm()
    db = get_db()

    if form.validate_on_submit():
        db.execute(
            """
            INSERT INTO imovel (cep, 
                                logradouro,
                                numero,
                                complemento,
                                bairro,
                                cidade, 
                                uf,
                                alugado,
                                id_locador)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                form.cep.data,
                form.logradouro.data,
                form.numero.data,
                form.complemento.data,
                form.bairro.data,
                form.cidade.data,
                form.uf.data,
                form.alugado.data,
                form.id_locador.data,
            ),
        )
        db.commit()
        flash("Cadastro Realizado com Sucesso.", "success")
        return redirect(url_for("imovel.imovel_list"))
    else:
        flash_errors(form)

    return render_template(
        "form.html",
        form=form,
        page_title=PAGE_TITLE,
    )


@imovel.route("/imovel/<int:id>", methods=["GET", "POST"])
def edit(id: int):
    db = get_db()
    form = ImovelForm()

    imovel = db.execute("SELECT * FROM imovel WHERE id = ?", (id,)).fetchone()
    if imovel is None:
        abort(404, "Imovel id {0} doesn't exist.".format(id))

    if request.method == "GET":
        form.cep.data = imovel["cep"]
        form.logradouro.data = imovel["logradouro"]
        form.numero.data = imovel["numero"]
        form.complemento.data = imovel["complemento"]
        form.bairro.data = imovel["bairro"]
        form.cidade.data = imovel["cidade"]
        form.uf.data = imovel["uf"]
        form.alugado.data = imovel["alugado"]
        form.id_locador.data = imovel["id_locador"]

    if form.validate_on_submit():
        db.execute(
            """
            UPDATE imovel 
            SET cep = ?,
                logradouro = ?,
                numero = ?,
                complemento = ?,
                bairro = ?,
                cidade = ?,
                uf = ?,
                alugado = ?,
                id_locador = ?
            WHERE id = ?
            """,
            (
                form.cep.data,
                form.logradouro.data,
                form.numero.data,
                form.complemento.data,
                form.bairro.data,
                form.cidade.data,
                form.uf.data,
                form.alugado.data,
                form.id_locador.data,
                id,
            ),
        )
        db.commit()
        flash("Cadastro Atualizado com Sucesso.", "success")
        return redirect(url_for("imovel.imovel_list"))

    return render_template("form.html", form=form, page_title="Editar Imovel")


@imovel.route("/imovel/<int:id>/delete/", methods=["GET", "POST"])
def delete(id: int):
    db = get_db()
    db.execute("DELETE FROM imovel WHERE id = ?", (id,))
    db.commit()
    flash("Imovel deletado com sucesso.", "success")
    return redirect(url_for("imovel.imovel_list"))
