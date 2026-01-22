from flask import Blueprint, render_template, request, redirect, url_for
from .models import Patient
from . import db

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    return redirect(url_for("main.dashboard"))


@main_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@main_bp.route("/patients", methods=["GET", "POST"])
def patients():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        diagnosis = request.form.get("diagnosis")

        patient = Patient(
            name=name,
            age=age,
            gender=gender,
            diagnosis=diagnosis
        )

        db.session.add(patient)
        db.session.commit()

        return redirect(url_for("main.patients"))

    patients = Patient.query.all()
    return render_template("patients.html", patients=patients)


@main_bp.route("/patients/edit/<int:patient_id>", methods=["GET", "POST"])
def edit_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)

    if request.method == "POST":
        patient.name = request.form.get("name")
        patient.age = request.form.get("age")
        patient.gender = request.form.get("gender")
        patient.diagnosis = request.form.get("diagnosis")

        db.session.commit()
        return redirect(url_for("main.patients"))

    return render_template("edit_patient.html", patient=patient)


@main_bp.route("/patients/delete/<int:patient_id>")
def delete_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    db.session.delete(patient)
    db.session.commit()
    return redirect(url_for("main.patients"))
