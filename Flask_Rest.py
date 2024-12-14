from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Create an uploads folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Simulated Prediction
    # Here, you can add your ML model processing code
    prediction = f"Received image: {file.filename}"

    # Optionally remove the file after prediction
    os.remove(file_path)

    return jsonify({"result": prediction})

if __name__ == '__main__':
    app.run(port=5001, debug=True)
