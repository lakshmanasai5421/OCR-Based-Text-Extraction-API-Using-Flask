from flask import Blueprint, request, jsonify
import pytesseract
from PIL import Image, UnidentifiedImageError
import requests
import io

ocr_bp = Blueprint('ocr', __name__)

def extract_text_from_image(image_file):
    """Performs OCR on an image using Tesseract"""
    try:
        image = Image.open(image_file).convert('L')
        text = pytesseract.image_to_string(image)
        return text.strip() if text.strip() else "No text found in image"
    except UnidentifiedImageError:
        return "Invalid image format"
    except Exception as e:
        return f"Error processing image: {e}"

@ocr_bp.route('/image', methods=['GET', 'POST'])
def extract_image():
    """Extracts text from an image (URL or file upload)"""
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        text = extract_text_from_image(file)
        return jsonify({"text": text})

    elif request.method == 'GET':
        url = request.args.get('url')
        if not url:
            return jsonify({"error": "No URL provided"}), 400
        response = requests.get(url, stream=True)
        if response.status_code != 200:
            return jsonify({"error": f"HTTP {response.status_code}"}), 400

        image_file = io.BytesIO(response.content)
        text = extract_text_from_image(image_file)
        return jsonify({"text": text})

    return jsonify({"error": "Invalid request"}), 405
