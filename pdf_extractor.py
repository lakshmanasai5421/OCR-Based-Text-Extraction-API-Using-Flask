from flask import Blueprint, request, jsonify
import pdfplumber
import requests
import io

pdf_bp = Blueprint('pdf', __name__)

def extract_text_from_pdf(pdf_file):
    """Extracts text from a PDF using pdfplumber"""
    text = ""
    try:
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                extracted_text = page.extract_text()
                if extracted_text:
                    text += extracted_text + "\n"
        return text.strip() if text.strip() else "No text found in PDF"
    except Exception as e:
        return f"Error processing PDF: {e}"

@pdf_bp.route('/pdf', methods=['GET', 'POST'])
def extract_pdf():
    """Extracts text from a PDF (URL or file upload)"""
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        text = extract_text_from_pdf(file)
        return jsonify({"text": text})

    elif request.method == 'GET':
        url = request.args.get('url')
        if not url:
            return jsonify({"error": "No URL provided"}), 400
        response = requests.get(url, stream=True)
        if response.status_code != 200:
            return jsonify({"error": f"HTTP {response.status_code}"}), 400

        pdf_file = io.BytesIO(response.content)
        text = extract_text_from_pdf(pdf_file)
        return jsonify({"text": text})

    return jsonify({"error": "Invalid request"}), 405
