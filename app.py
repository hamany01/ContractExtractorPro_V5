from flask import Flask, request, jsonify
from contract_text_extractor import extract_contract_data

# هذا هو المتغير الذي يبحث عنه Gunicorn
app = Flask(__name__)

@app.route('/')
def home():
    return "مرحبًا بك في ContractExtractorPro V5 - التطبيق يعمل ✅"

@app.route('/extract', methods=['POST'])
def extract():
    if 'text' not in request.json:
        return jsonify({"error": "يجب إرسال نص العقد ضمن الحقل 'text'"}), 400

    text = request.json['text']
    try:
        extracted_data = extract_contract_data(text)
        return jsonify(extracted_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)