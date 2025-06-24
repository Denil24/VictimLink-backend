from flask import Blueprint, request, jsonify
from app.utils.hashing import generate_sha256
from app.utils.classifier import classify_text
from app.utils.mongo import collection  # ✅ MongoDB collection
import time  # for timestamp

upload_bp = Blueprint('upload_bp', __name__)

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    file_bytes = file.read()
    text = file_bytes.decode(errors='ignore')

    sha256 = generate_sha256(file_bytes)
    abuse_type, score = classify_text(text)

    # ✅ Save to MongoDB
    log = {
        "filename": file.filename,
        "sha256_hash": sha256,
        "abuse_type": abuse_type,
        "confidence": score,
        "timestamp": time.time()
    }
    collection.insert_one(log)

    return jsonify({
        'filename': file.filename,
        'sha256_hash': sha256,
        'abuse_type': abuse_type,
        'confidence': score
    })
