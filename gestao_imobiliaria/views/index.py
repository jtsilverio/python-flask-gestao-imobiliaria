from flask import Blueprint, render_template

index = Blueprint("index", __name__)
PAGE_NAME = "index"


@index.route("/")
def index_page():
    PAGE_TITLE = PAGE_NAME
    return render_template(
        "home.html",
        page_title=PAGE_TITLE,
        blueprint=PAGE_NAME,
    )
