import os
import secrets

import dotenv
from flask import Flask
from datetime import datetime

dotenv.load_dotenv()
os.environ["SECRET_KEY"] = secrets.token_urlsafe(16)


def create_app():
    from gestao_imobiliaria import db
    from gestao_imobiliaria.views.contrato import contrato
    from gestao_imobiliaria.views.imovel import imovel
    from gestao_imobiliaria.views.index import index
    from gestao_imobiliaria.views.locador import locador
    from gestao_imobiliaria.views.locatario import locatario

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY"),
        DATABASE=os.getenv("DATABASE"),
    )
    app.jinja_env.globals.update(datetime=datetime)
    
    with app.app_context():
        db.init_app(app)

    app.register_blueprint(locador)
    app.register_blueprint(locatario)
    app.register_blueprint(imovel)
    app.register_blueprint(contrato)
    app.register_blueprint(index)

    return app
