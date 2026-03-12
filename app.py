from flask import Flask, render_template, request, jsonify
import math
import re
import PyPDF2
import docx

app = Flask(__name__)

# --- THE COGNITIVE FOCUS ENGINE ---
def apply_cognitive_focus(raw_text):
    words = raw_text.split()
    formatted_words = []
    for word in words:
        match = re.match(r'^(\W*)([\w\-\']+)(\W*)$', word)
        if match:
            prefix, core, suffix = match.groups()
            length = len(core)
            if length == 0:
                formatted_words.append(word)
            elif length == 1:
                formatted_words.append(f"{prefix}<b>{core}</b>{suffix}")
            else:
                midpoint = math.ceil(length / 2)
                first_half = core[:midpoint]
                second_half = core[midpoint:]
                formatted_words.append(f"{prefix}<b>{first_half}</b>{second_half}{suffix}")
        else:
            formatted_words.append(word)
    return " ".join(formatted_words)

# --- ROUTES ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'document' not in request.files:
        return jsonify({'error': 'No file uploaded.'}), 400
    
    file = request.files['document']
    if file.filename == '':
        return jsonify({'error': 'No file selected.'}), 400
    
    file_ext = file.filename.lower().split('.')[-1]
    raw_text = ""

    try:
        if file_ext == 'txt':
            raw_text = file.read().decode('utf-8')
        elif file_ext == 'pdf':
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                extracted = page.extract_text()
                if extracted:
                    raw_text += extracted + "\n\n"
        elif file_ext == 'docx':
            doc = docx.Document(file)
            for para in doc.paragraphs:
                raw_text += para.text + "\n\n"
        else:
             return jsonify({'error': 'Please upload .txt, .pdf, or .docx'}), 400

        if not raw_text.strip():
            return jsonify({'error': 'The document appears to be empty or unreadable.'}), 400

        formatted_html = apply_cognitive_focus(raw_text)
        return jsonify({'formatted_text': formatted_html})

    except Exception as e:
        return jsonify({'error': f'Processing failed: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)