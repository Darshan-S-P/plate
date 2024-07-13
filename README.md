# License Plate Recognition Project

This project implements a license plate recognition system using Python and Flask.

## Deployment

The application is deployed and accessible via PythonAnywhere:

[License Plate Recognition App](http://DarshanSP.pythonanywhere.com)

## Installation

To run this project locally, follow these steps...
To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd license-plate-recognition
   
2.**Create a virtual environment (optional but recommended)**:
```bash
python -m venv venv
source venv/bin/activate
```

3.Install dependencies:
```bash
pip install -r requirements.txt
```

4.Set up Tesseract OCR (if not installed):

Install Tesseract OCR: Tesseract OCR Installation Guide
Update the Tesseract path in app.py if necessary:
pytesseract.pytesseract.tesseract_cmd = '/path/to/your/tesseract'

5.Run the application:
```bash
python app.py
```

6.Access the application at http://localhost:5000 in your browser.

## Usage

1.Open the application in your browser.
2.Upload an image containing a license plate using the provided upload button.
3.Click the "Submit" button.
4.The application will process the image and display the recognized license plate number.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
