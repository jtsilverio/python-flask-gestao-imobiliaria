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
from gestao_imobiliaria.forms import LocadorForm
from gestao_imobiliaria.views.utils import flash_errors, get_column_names

locador = Blueprint("locador", __name__)
PAGE_NAME = "locador"


@locador.route("/locador/")
def locador_list():
    PAGE_TITLE = PAGE_NAME
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
        blueprint=PAGE_NAME,
    )


@locador.route("/locador/cadastro/", methods=["GET", "POST"])
def cadastro():
    PAGE_TITLE = "cadastro locador"
    form = LocadorForm()
    db = get_db()

    if form.validate_on_submit():
        db = get_db()
        db.execute(
            """
            INSERT INTO locador (primeiro_nome, ultimo_nome, email,
                                ddd, telefone, tipo_logradouro, 
                                endereco, numero, cep) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                form.primeiro_nome.data,
                form.ultimo_nome.data,
                form.email.data,
                form.ddd.data,
                form.telefone.data,
                form.tipo_logradouro.data,
                form.endereco.data,
                form.numero.data,
                form.cep.data,
            ),
        )
        db.commit()
        flash("Cadastro Realizado com Sucesso.", "success")
        return redirect(url_for("locador_form"))
    else:
        flash_errors(form)

    return render_template(
        "form.html",
        form=form,
        page_title=PAGE_TITLE,
    )


@locador.route("/locador/<int:id>", methods=["GET", "POST"])
def edit(id: int):
    db = get_db()
    form = LocadorForm()

    locador = db.execute("SELECT * FROM locador WHERE id = ?", (id,)).fetchone()
    if locador is None:
        abort(404, "Locador id {0} doesn't exist.".format(id))

    if request.method == "GET":
        form.primeiro_nome.data = locador["primeiro_nome"]
        form.ultimo_nome.data = locador["ultimo_nome"]
        form.email.data = locador["email"]
        form.ddd.data = locador["ddd"]
        form.telefone.data = locador["telefone"]
        form.tipo_logradouro.data = locador["tipo_logradouro"]
        form.endereco.data = locador["endereco"]
        form.numero.data = locador["numero"]
        form.cep.data = locador["cep"]

    if form.validate_on_submit():
        db.execute(
            """
            UPDATE locador 
                SET primeiro_nome = ?,
                ultimo_nome = ?,
                email = ?,
                ddd = ?,
                telefone = ?,
                tipo_logradouro =
                ?, 
                endereco = ?,
                numero = ?,
                cep = ?
            WHERE id = ?
            """,
            (
                form.primeiro_nome.data,
                form.ultimo_nome.data,
                form.email.data,
                form.ddd.data,
                form.telefone.data,
                form.tipo_logradouro.data,
                form.endereco.data,
                form.numero.data,
                form.cep.data,
                id,
            ),
        )
        db.commit()
        flash("Cadastro Atualizado com Sucesso.", "success")
        return redirect(url_for("locador_list"))

    return render_template("form.html", form=form, page_title="Editar Locador")


@locador.route("/locador/<int:id>/delete/", methods=["GET", "POST"])
def delete(id: int):
    db = get_db()
    db.execute("DELETE FROM locador WHERE id = ?", (id,))
    db.commit()
    flash("Locador deletado com sucesso.", "success")
    return redirect(url_for("locador_list"))
