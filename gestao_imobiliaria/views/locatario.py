from flask import Blueprint, abort, flash, redirect, render_template, request, url_for

from gestao_imobiliaria.db import get_db
from gestao_imobiliaria.views.utils import get_column_names

locatario = Blueprint("locatario", __name__)
from gestao_imobiliaria.forms import LocatarioForm
from gestao_imobiliaria.views.utils import flash_errors, get_column_names

PAGE_NAME = "locatario"


@locatario.route("/locatario/")
def locatario_list():
    PAGE_TITLE = PAGE_NAME
    db = get_db()
    colunas = get_column_names(db, table="locatario")

    dados = db.execute(
        """
        SELECT *
        FROM locatario
        ORDER BY id DESC;
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


@locatario.route("/locatario/cadastro/", methods=["GET", "POST"])
def cadastro():
    PAGE_TITLE = "cadastro locatário"
    form = LocatarioForm()
    db = get_db()

    if form.validate_on_submit():
        db.execute(
            """
            INSERT INTO locatario (cpf, primeiro_nome, ultimo_nome, email,
                                ddd, telefone, cep, 
                                logradouro, numero, complemento, bairro, cidade, uf) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                form.cpf.data,
                form.primeiro_nome.data,
                form.ultimo_nome.data,
                form.email.data,
                form.ddd.data,
                form.telefone.data,
                form.cep.data,
                form.logradouro.data,
                form.numero.data,
                form.complemento.data,
                form.bairro.data,
                form.cidade.data,
                form.uf.data,
            ),
        )
        db.commit()
        flash("Cadastro Realizado com Sucesso.", "success")
        return redirect(url_for("locatario.locatario_list"))
    else:
        flash_errors(form)

    return render_template(
        "form.html",
        form=form,
        page_title=PAGE_TITLE,
    )


@locatario.route("/locatario/<int:id>", methods=["GET", "POST"])
def edit(id: int):
    db = get_db()
    form = LocatarioForm()

    locatario = db.execute("SELECT * FROM locatario WHERE id = ?", (id,)).fetchone()
    if locatario is None:
        abort(404, "Locatario id {0} doesn't exist.".format(id))

    if request.method == "GET":
        form.cpf.data = locatario["cpf"]
        form.primeiro_nome.data = locatario["primeiro_nome"]
        form.ultimo_nome.data = locatario["ultimo_nome"]
        form.email.data = locatario["email"]
        form.ddd.data = locatario["ddd"]
        form.telefone.data = locatario["telefone"]
        form.cep.data = locatario["cep"]
        form.logradouro.data = locatario["logradouro"]
        form.numero.data = locatario["numero"]
        form.complemento.data = locatario["complemento"]
        form.bairro.data = locatario["bairro"]
        form.cidade.data = locatario["cidade"]
        form.uf.data = locatario["uf"]

    if form.validate_on_submit():
        db.execute(
            """
            UPDATE locatario 
            SET cpf = ?,
                primeiro_nome = ?,
                ultimo_nome = ?,
                email = ?,
                ddd = ?,
                telefone = ?,
                cep = ?,
                logradouro = ?,
                numero = ?,
                complemento = ?,
                bairro = ?,
                cidade = ?,
                uf = ?
            WHERE id = ?
            """,
            (
                form.cpf.data,
                form.primeiro_nome.data,
                form.ultimo_nome.data,
                form.email.data,
                form.ddd.data,
                form.telefone.data,
                form.cep.data,
                form.logradouro.data,
                form.numero.data,
                form.complemento.data,
                form.bairro.data,
                form.cidade.data,
                form.uf.data,
                id,
            ),
        )
        db.commit()
        flash("Cadastro Atualizado com Sucesso.", "success")
        return redirect(url_for("locatario.locatario_list"))

    return render_template("form.html", form=form, page_title="Editar Locatario")


@locatario.route("/locatario/<int:id>/delete/", methods=["GET", "POST"])
def delete(id: int):
    db = get_db()
    db.execute("DELETE FROM locatario WHERE id = ?", (id,))
    db.commit()
    flash("Locatario deletado com sucesso.", "success")
    return redirect(url_for("locatario.locatario_list"))
