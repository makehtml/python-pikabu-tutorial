from flask import Blueprint, render_template

core = Blueprint("core", __name__, template_folder="templates")


@core.route("/index")
@core.route("/")
def index():
    return render_template("index.j2")