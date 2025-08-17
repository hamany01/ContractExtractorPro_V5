from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from . import db
from .models import Document
from .utils import save_file
from .ai_analysis import analyze_document

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("home.html")


@main.route("/dashboard")
@login_required
def dashboard():
    documents = Document.query.filter_by(user_id=current_user.id).all()
    return render_template("dashboard.html", documents=documents)


@main.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    if request.method == "POST":
        file = request.files.get("file")
        if not file or file.filename == "":
            flash("الرجاء اختيار ملف", "warning")
            return redirect(url_for("main.upload"))
        try:
            path = save_file(file)
            result = analyze_document(path)
            document = Document(filename=file.filename, result=str(result), user_id=current_user.id)
            db.session.add(document)
            db.session.commit()
            flash("تم رفع الملف وتحليله", "success")
            return redirect(url_for("main.dashboard"))
        except Exception as exc:
            flash(str(exc), "danger")
            return redirect(url_for("main.upload"))
    return render_template("upload.html")
