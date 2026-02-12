import os
from flask import Blueprint, render_template, request, jsonify, current_app, send_from_directory
from werkzeug.utils import secure_filename
from app.converters import PDFConverter, EPUBConverter, ImageConverter, MarkdownConverter
main_bp = Blueprint('main', __name__)
@main_bp.route('/')
def index():
    return render_template('index.html')
@main_bp.route('/api/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return jsonify({"success": False, "error": "Arquivo não enviado"}), 400
    file = request.files['file']
    conversion_type = request.form.get('conversion_type') 
    if file.filename == '':
        return jsonify({"success": False, "error": "Nome inválido"}), 400
    filename = secure_filename(file.filename)
    input_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(input_path)

    try:
        if 'pdf' in conversion_type and 'epub' not in conversion_type:
            conv = PDFConverter()
            method = getattr(conv, conversion_type)
        elif 'epub' in conversion_type:
            conv = EPUBConverter()
            method = getattr(conv, conversion_type)
        elif 'image' in conversion_type:
            conv = ImageConverter()
            method = getattr(conv, conversion_type)
        elif 'markdown' in conversion_type:
            conv = MarkdownConverter()
            method = getattr(conv, conversion_type)
        else:
            raise Exception("Tipo de conversão não suportado")
        output_path = method(input_path)
        output_filename = os.path.basename(output_path)
        return jsonify({
            "success": True,
            "filename": output_filename,
            "download_url": f"/download/{output_filename}"
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
@main_bp.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(current_app.config['CONVERTED_FOLDER'], filename, as_attachment=True)