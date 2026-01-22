from flask import Blueprint, render_template, redirect, url_for, session
from .models import Patient, Staff

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return redirect(url_for("auth.login"))


@main.route("/dashboard")
def dashboard():
    if "admin_id" not in session:
        return redirect(url_for("auth.login"))

    patient_count = Patient.query.count()
    staff_count = Staff.query.count()

    return render_template(
        "dashboard.html",
        patient_count=patient_count,
        staff_count=staff_count
    )

