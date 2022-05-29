"""
Here should be some docstring for views.py
"""
from flask import Blueprint, render_template

core = Blueprint("core", __name__, template_folder="templates")


@core.route("/index")
@core.route("/")
def index():
    return 'OK'  # render_template("pages/index.j2")