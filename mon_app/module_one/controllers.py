
from flask import Blueprint, request, render_template

module_one = Blueprint(__name__)

@module_one.route("/")
def home():
    return render_template("module_one/index.html")