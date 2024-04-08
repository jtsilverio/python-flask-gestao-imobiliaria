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
    primeiro_nome = StringField("Primeiro Nome")
    ultimo_nome = StringField("Sobrenome")
    email = StringField("CPF")
    ddd = IntegerField("DDD")
    telefone = StringField("Telefone")
    tipo_logradouro = StringField("Tipo de Logradouro")
    endereco = StringField("Endereço")
    numero = IntegerField("Número")
    cep = StringField("CEP")


class ImovelForm(FlaskForm):
    endereco_logradouro = StringField("Endereço")
    endereco_numero = StringField("Número")
    endereco_complemento = StringField("Complemento")
    endereco_bairro = StringField("Bairro")
    endereco_cidade = StringField("Cidade")
    endereco_estado = StringField("Estado")
    endereco_cep = StringField("CEP")
    alugado = SelectField("Alugado")
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
    primeiro_nome = StringField("Primeiro Nome")
    ultimo_nome = StringField("Sobrenome")
    email = StringField("CPF")
    ddd = IntegerField("DDD")
    telefone = StringField("Telefone")
    tipo_logradouro = StringField("Tipo de Logradouro")
    endereco = StringField("Endereço")
    numero = IntegerField("Número")
    cep = StringField("CEP")
    submit = SubmitField("Salvar")
