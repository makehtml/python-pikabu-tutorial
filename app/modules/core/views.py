"""
Here should be some docstring for views.py
"""
from flask import Blueprint, render_template

from app.modules.navi.models import Message

core = Blueprint("core", __name__, template_folder="templates")


@core.route("/index")
@core.route("/")
def index():
    return render_template("index.j2")


@core.route("/show")
def show():
    messages = Message.query.all()
    return render_template("show.j2", messages=messages)
