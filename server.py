from flask import Flask
from ocr import ocr_bp
from pdf_extractor import pdf_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(ocr_bp, url_prefix='/extract')
app.register_blueprint(pdf_bp, url_prefix='/extract')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
