from flask import Flask, request, render_template, redirect, url_for
import cv2
import pytesseract
import os

# Path to the Tesseract executable (if not added to PATH)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust the path as needed

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        text = detect_number_plate(file_path)
        return render_template('index.html', text=text)

def detect_number_plate(image_path):
    harcascade = "model/haarcascade_russian_plate_number.xml"
    min_area = 500

    # Load the image
    img = cv2.imread(image_path)

    if img is None:
        return "Error: Could not load image."
    else:
        plate_cascade = cv2.CascadeClassifier(harcascade)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)
        
        detected_texts = []

        for (x, y, w, h) in plates:
            area = w * h   
            
            if area > min_area:
                img_roi = img[y: y + h, x: x + w]
                
                # OCR to read the number plate
                text = pytesseract.image_to_string(img_roi, config='--psm 8')  # psm 8 treats the image as a single word
                detected_texts.append(text.strip())
        
        return "\n".join(detected_texts)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
