from flask import Flask, request, render_template, redirect, url_for, flash
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "your_secret_key"  # For flash messages

# Load AI Model
model = load_model("chest_disease_model.keras")

# Define your classes
class_names = ['COVID-19', 'Normal', 'Pneumonia', 'Tuberculosis', 'Other_Lung_Infection']

# Upload folder and allowed extensions
UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure uploads folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/upload", methods=['GET', 'POST'])
def upload_xray():
    if request.method == 'POST':
        if 'xray' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['xray']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Preprocess image
            img = Image.open(filepath).convert("RGB")
            img = img.resize((224, 224))
            img_array = image.img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            # Prediction
            preds = model.predict(img_array)
            predicted_class = np.argmax(preds, axis=1)[0]
            confidence = np.max(preds)

            diagnosis = class_names[predicted_class]
            confidence = round(float(confidence)*100, 2)

            return render_template('result.html',
                                   diagnosis=diagnosis,
                                   confidence=confidence,
                                   image_path=filename)
        else:
            flash('Invalid file format. Please upload a JPG or PNG image.')
            return redirect(request.url)

    return render_template('upload.html')

# For serving uploaded images in result.html
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return redirect(url_for('static', filename=f'uploads/{filename}'))

if __name__ == "__main__":
    app.run(debug=True)
