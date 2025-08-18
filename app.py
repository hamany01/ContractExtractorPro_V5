# app.py - ملف التشغيل الرئيسي للتطبيق

from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>أهلاً بك في ContractExtractorPro V5</h1><p>تم نشر التطبيق بنجاح!</p>"

# يمكنك إضافة مسارات إضافية هنا
# مثال:
# @app.route('/upload', methods=['POST'])
# def upload():
#     return "Upload handler"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
