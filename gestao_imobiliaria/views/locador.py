from flask import current_app, flash, redirect, render_template, url_for

from gestao_imobiliaria.db import get_db
from gestao_imobiliaria.forms import LocadorForm
from gestao_imobiliaria.views.utils import flash_errors, get_column_names


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


@current_app.route("/locador/cadastro/", methods=["GET", "POST"])
def locador_form():
    PAGE_TITLE = "cadastro locador"
    form = LocadorForm()

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
        "cadastro.html",
        form=form,
        page_title=PAGE_TITLE,
    )
