from flask import current_app, render_template


@current_app.route("/")
def index():
    PAGE_TITLE = "home"
    return render_template("home.html", page_title=PAGE_TITLE)
