import os
from flask import current_app
from werkzeug.utils import secure_filename


def allowed_file(filename: str) -> bool:
    """التحقق من امتداد الملف المسموح به."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in current_app.config["ALLOWED_EXTENSIONS"]


def save_file(file) -> str:
    """حفظ الملف المرفوع وإرجاع مساره."""
    if not allowed_file(file.filename):
        raise ValueError("امتداد الملف غير مسموح")
    filename = secure_filename(file.filename)
    upload_folder = current_app.config["UPLOAD_FOLDER"]
    os.makedirs(upload_folder, exist_ok=True)
    path = os.path.join(upload_folder, filename)
    file.save(path)
    return path
