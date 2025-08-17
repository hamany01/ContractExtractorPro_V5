# init_db.py
import os
from app import db

# تأكد من وجود مجلد database
if not os.path.exists('database'):
    os.makedirs('database')

# إنشاء قاعدة البيانات
db.create_all()
print("✔️ تم إنشاء قاعدة البيانات بنجاح داخل database/data.db")
