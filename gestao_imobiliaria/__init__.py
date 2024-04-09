import os
import secrets

import dotenv
from flask import Flask

dotenv.load_dotenv()
os.environ["SECRET_KEY"] = secrets.token_urlsafe(16)


def create_app():
    from gestao_imobiliaria import db

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY"),
        DATABASE=os.getenv("DATABASE"),
    )
    db.init_app(app)

    with app.app_context():
        from gestao_imobiliaria import views  # noqa

    from gestao_imobiliaria.views.locador import locador

    app.register_blueprint(locador)
    return app
