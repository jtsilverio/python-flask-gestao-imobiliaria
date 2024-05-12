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
    alugado = SelectField("Alugado", choices=[("Não", "Não"), ("Sim", "Sim")])
    id_locador = SelectField("Locador")
    submit = SubmitField("Salvar")


class ContratoForm(FlaskForm):
    def __init__(self, *args, edit=False, **kwargs):
        super(ContratoForm, self).__init__(*args, **kwargs)
        self.edit = edit
        self.populate_choices()

    def populate_choices(self):
        db = get_db()  # Get the database connection
        cursor = db.cursor()
        
        cursor.execute('SELECT id, primeiro_nome, ultimo_nome, cpf FROM locatario')
        rows = cursor.fetchall()
        self.id_locatario.choices = [(row['id'], f"{row['cpf']}: {row['primeiro_nome']} {row['ultimo_nome']}") for row in rows]
        
        if self.edit == False:
            cursor.execute("SELECT id, cep, logradouro, numero FROM imovel where alugado = 'Não'")
        else:
            cursor.execute("SELECT id, cep, logradouro, numero FROM imovel")
            
        rows = cursor.fetchall()
        self.id_imovel.choices = [(row['id'], f"{row['cep']}: {row['logradouro']}, {row['numero']}") for row in rows]
        
    data_inicio = DateField("Data de Início", format='%Y-%m-%d')
    data_fim = DateField("Data de Fim", format='%Y-%m-%d')
    valor_aluguel = FloatField("Valor do Aluguel")
    IPTU = FloatField("IPTU")
    condominio = FloatField("Condomínio", default=0)
    garantia = FloatField("Garantia", default=0)
    outras_despesas = FloatField("Outras Despesas", default=0)
    porcentagem_comissao = FloatField("Porcentagem de Comissão", default=0)
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
