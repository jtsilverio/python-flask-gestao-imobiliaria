from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    FloatField,
    IntegerField,
    SelectField,
    StringField,
    SubmitField,
)
from gestao_imobiliaria.db import get_db


class LocatarioForm(FlaskForm):
    cpf = StringField("CPF")
    primeiro_nome = StringField("Primeiro Nome")
    ultimo_nome = StringField("Sobrenome")
    email = StringField("CPF")
    ddd = IntegerField("DDD")
    telefone = StringField("Telefone")
    cep = StringField("CEP")
    logradouro = StringField("Tipo de Logradouro")
    numero = IntegerField("Número")
    complemento = StringField("Complemento")
    bairro = StringField("Bairro")
    cidade = StringField("Cidade")
    uf = StringField("UF")
    submit = SubmitField("Salvar")


class ImovelForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super(ImovelForm, self).__init__(*args, **kwargs)
        self.populate_choices()

    def populate_choices(self):
        db = get_db()  # Get the database connection
        cursor = db.cursor()
        cursor.execute('SELECT id, primeiro_nome, ultimo_nome, cpf FROM locador')
        rows = cursor.fetchall()
        self.id_locador.choices = [(row['id'], f"{row['cpf']}: {row['primeiro_nome']} {row['ultimo_nome']}") for row in rows]
    
    cep = StringField("CEP")
    logradouro = StringField("Logradouro")
    numero = IntegerField("Número")
    complemento = StringField("Complemento")
    bairro = StringField("Bairro")
    cidade = StringField("Cidade")
    uf = StringField("UF")
    alugado = SelectField("Alugado", choices=[("0", "Não"), ("1", "Sim")])
    id_locador = SelectField("Locador")
    submit = SubmitField("Salvar")


class ContratoForm(FlaskForm):
    data_inicio = DateField("Data de Início")
    data_fim = DateField("Data de Fim")
    valor_aluguel = FloatField("Valor do Aluguel")
    IPTU = FloatField("IPTU")
    condominio = FloatField("Condomínio")
    garantia = FloatField("Garantia")
    outras_despesas = FloatField("Outras Despesas")
    porcentagem_comissao = FloatField("Porcentagem de Comissão")
    id_imovel = SelectField("Imóvel")
    id_locatario = SelectField("Locatário")
    submit = SubmitField("Salvar")


class LocadorForm(FlaskForm):
    cpf = StringField("CPF")
    primeiro_nome = StringField("Primeiro Nome")
    ultimo_nome = StringField("Sobrenome")
    email = StringField("Email")
    ddd = IntegerField("DDD")
    telefone = StringField("Telefone")
    cep = StringField("CEP")
    logradouro = StringField("Logradouro")
    numero = IntegerField("Número")
    complemento = StringField("Complemento")
    bairro = StringField("Bairro")
    cidade = StringField("Cidade")
    uf = StringField("UF")
    submit = SubmitField("Salvar")
