from flask import render_template, redirect, url_for
from flask_login import login_required
from . import db

def register_routes(app):
    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/dashboard")
    @login_required
    def dashboard():
        return render_template("dashboard.html")