from flask import Blueprint, render_template, request, redirect, url_for
from .models import Admin
from . import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Login logic will be added later
        return redirect(url_for("main.dashboard"))

    return render_template("login.html")
