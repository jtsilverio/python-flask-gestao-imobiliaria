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
        SELECT *
        FROM locador
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


@locador.route("/locador/cadastro/", methods=["GET", "POST"])
def cadastro():
    PAGE_TITLE = "cadastro locador"
    form = LocadorForm()
    db = get_db()

    if form.validate_on_submit():
        db.execute(
            """
            INSERT INTO locador (cpf, primeiro_nome, ultimo_nome, email,
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
        return redirect(url_for("locador.locador_list"))
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
        form.cpf.data = locador["cpf"]
        form.primeiro_nome.data = locador["primeiro_nome"]
        form.ultimo_nome.data = locador["ultimo_nome"]
        form.email.data = locador["email"]
        form.ddd.data = locador["ddd"]
        form.telefone.data = locador["telefone"]
        form.cep.data = locador["cep"]
        form.logradouro.data = locador["logradouro"]
        form.numero.data = locador["numero"]
        form.complemento.data = locador["complemento"]
        form.bairro.data = locador["bairro"]
        form.cidade.data = locador["cidade"]
        form.uf.data = locador["uf"]

    if form.validate_on_submit():
        db.execute(
            """
            UPDATE locador 
            SET cpf = ?,
                primeiro_nome = ?,
                ultimo_nome = ?,
                email = ?,
                ddd = ?,
                telefone = ?,
                cep = ?,
                logradouro = ?,
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
        return redirect(url_for("locador.locador_list"))

    return render_template("form.html", form=form, page_title="Editar Locador")


@locador.route("/locador/<int:id>/delete/", methods=["GET", "POST"])
def delete(id: int):
    db = get_db()
    db.execute("DELETE FROM locador WHERE id = ?", (id,))
    db.commit()
    flash("Locador deletado com sucesso.", "success")
    return redirect(url_for("locador.locador_list"))
