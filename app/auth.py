from flask import Blueprint, render_template, request, redirect, url_for, session
from .models import Admin

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        admin = Admin.query.filter_by(username=username).first()
        if admin and admin.check_password(password):
            session["admin_id"] = admin.id
            return redirect(url_for("main.dashboard"))

        return "Invalid credentials", 401

    return render_template("login.html")


@auth.route("/logout")
def logout():
    session.pop("admin_id", None)
    return redirect(url_for("auth.login"))

