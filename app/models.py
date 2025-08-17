from datetime import datetime

from flask_login import UserMixin

from . import db, login_manager

class User(UserMixin, db.Model):
    """مستخدمو النظام."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


class Document(db.Model):
    """تمثيل ملف تم رفعه وتحليله."""

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    result = db.Column(db.Text, nullable=True)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


@login_manager.user_loader
def load_user(user_id: str):
    return User.query.get(int(user_id))