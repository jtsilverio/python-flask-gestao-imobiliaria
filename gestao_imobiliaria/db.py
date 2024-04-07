import os
import sqlite3

import click
from flask import g


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            os.getenv("DATABASE_URL"), detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


@click.command("init-db")
def init_db():
    if not os.path.exists(os.getenv("DATABASE_URL")):
        db = get_db()
        with open("database/schema.sql") as sql_create_script:
            db.executescript(sql_create_script.read())


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db)


if __name__ == "__main__":
    init_db()
