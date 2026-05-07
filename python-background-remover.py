from flask import Flask, render_template, request, send_file, jsonify
from rembg import remove
from PIL import Image
import os
from werkzeug.utils import secure_filename
import io

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

# Create uploads folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def remove_bg_from_image(image_path):
    """Remove background from image using rembg"""
    try:
        with open(image_path, 'rb') as i:
            input_data = i.read()
        output_data = remove(input_data)
        output_image = Image.open(io.BytesIO(output_data))
        return output_image
    except Exception as e:
        raise Exception(f"Error processing image: {str(e)}")

@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and background removal"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Check file extension
        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}
        if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
            return jsonify({'error': 'Invalid file type. Please upload an image.'}), 400
        
        # Save uploaded file temporarily
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Remove background
        output_image = remove_bg_from_image(filepath)
        
        # Convert to bytes for download
        img_io = io.BytesIO()
        output_image.save(img_io, 'PNG')
        img_io.seek(0)
        
        # Clean up temp file
        os.remove(filepath)
        
        return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='output_image.png')
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)

