from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"

# قاعدة البيانات
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, 'database', 'data.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# نموذج قاعدة البيانات - مثال
class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)

# الصفحة الرئيسية
@app.route('/')
def home():
    contracts = Contract.query.all()
    return render_template('index.html', contracts=contracts)

# صفحة إضافة عقد جديد
@app.route('/add', methods=['GET', 'POST'])
def add_contract():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_contract = Contract(title=title, content=content)
        db.session.add(new_contract)
        db.session.commit()
        flash('تمت إضافة العقد بنجاح', 'success')
        return redirect(url_for('home'))
    return render_template('add_contract.html')

# نقطة البداية عند التشغيل المحلي (اختياري لـ development فقط)
if __name__ == '__main__':
    app.run(debug=True)
