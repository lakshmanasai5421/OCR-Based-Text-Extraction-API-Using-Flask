# OCR-Based Text Extraction API Using Flask & PHP

## 📌 Project Overview
This project provides an **OCR-based text extraction API** using Flask and integrates with a PHP client for uploading images and PDFs. The API extracts text from:
- **Images** using **Tesseract OCR**.
- **PDFs** using **pdfplumber**.

The **Flask server** processes the files, while the **PHP frontend** allows users to upload images or PDFs and view the extracted text.

---

## 🚀 Features
✔ Extract text from images using **OCR (Tesseract)**  
✔ Extract text from PDFs using **pdfplumber**  
✔ API accessible via **Flask Blueprint routing**  
✔ PHP interface for easy file uploads  
✔ Supports **both file uploads and URLs**  

---

## 📂 Project Structure
```
/project_folder
│── server.py              # Main Flask server
│── ocr.py                 # OCR-based image text extraction
│── pdf_extractor.py        # PDF text extraction
│── client.php              # PHP client for file uploads
```

---

## 🔧 Pre-requirements
Before running this project, ensure you have the following:

### **1️⃣ Install Python (3.8 or higher)**
Check if Python is installed:
```cmd
python --version
```

### **2️⃣ Install PHP (for Client)**
Check if PHP is installed:
```cmd
php -v
```

### **3️⃣ Install Required Python Modules**
Run the following command:
```cmd
pip install flask requests pdfplumber pytesseract pillow
```

---

## 📦 Python Modules & Versions
| Module      | Version  |
|------------|---------|
| Flask      | 3.0.0   |
| requests   | 2.31.0  |
| pdfplumber | 0.9.0   |
| pytesseract | 0.3.10  |
| Pillow     | 10.0.1  |

---

## 🚀 Running the Project
### **1️⃣ Start Flask Server**
Run the following command:
```cmd
python server.py
```

---

## 🔗 API Endpoints

### **Test with Your Example Image**
Open in browser (For OCR Image):
```
http://127.0.0.1:5000/extract/image?url=https://thumbs.dreamstime.com/z/old-newspaper-design-vector-template-vintage-retro-background-text-images-77345579.jpg
```

### **Test with Your Example PDF**
Open in browser (For PDF extraction):
```
http://127.0.0.1:5000/extract/pdf?url=https://arxiv.org/pdf/1706.03762.pdf
```

