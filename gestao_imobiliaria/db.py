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
def init_db_command():
    init_db()
    click.echo("Initialized the database.")


def init_db():
    print(os.getenv("DATABASE_URL"))
    if not os.path.exists(os.getenv("DATABASE_URL")):
        db = get_db()
        print("Database not found")
        with open("database/schema.sql") as sql_create_script:
            db.executescript(sql_create_script.read())
            print("Database created")


def init_app(app):
    init_db()
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


if __name__ == "__main__":
    init_db()
