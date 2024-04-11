from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    FloatField,
    IntegerField,
    SelectField,
    StringField,
    SubmitField,
)


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
    cep = StringField("CEP")
    logradouro = StringField("Logradouro")
    numero = IntegerField("Número")
    complemento = StringField("Complemento")
    bairro = StringField("Bairro")
    cidade = StringField("Cidade")
    uf = StringField("UF")
    alugado = SelectField("Alugado")
    locador = SelectField("Locador")
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
