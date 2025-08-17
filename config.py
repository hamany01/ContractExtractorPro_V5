import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-me")
    UPLOAD_FOLDER = os.path.join("data", "uploads")
    ALLOWED_EXTENSIONS = {"pdf", "docx", "xlsx"}
    SQLALCHEMY_DATABASE_URI = "sqlite:///instance/app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False