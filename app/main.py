from flask import Flask, jsonify
from flask_cors import CORS
from app.routes.upload import upload_bp
from app.utils.mongo import collection
import os

app = Flask(__name__)
CORS(app)
app.register_blueprint(upload_bp)

@app.route('/')
def index():
    return "VictimLink Backend is Running ✅"

@app.route('/dbstatus')
def db_status():
    try:
        collection.database.command("ping")
        return jsonify({"status": "MongoDB connection successful ✅"}), 200
    except Exception as e:
        return jsonify({
            "status": "MongoDB connection failed ❌",
            "error": str(e)
        }), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # ✅ Use PORT env if available
    app.run(host="0.0.0.0", port=port)
