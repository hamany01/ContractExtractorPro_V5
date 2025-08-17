# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "🎉 مرحبًا بك في JPF Contract Analyzer - الإصدار 5"

if __name__ == "__main__":
    app.run(debug=True)
