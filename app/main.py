from flask import Flask, jsonify
from flask_cors import CORS
from app.routes.upload import upload_bp
from app.utils.mongo import collection  # ✅ MongoDB connection

app = Flask(__name__)
CORS(app)
app.register_blueprint(upload_bp)

@app.route('/')
def index():
    return "VictimLink Backend is Running ✅"

# ✅ MongoDB Connection Test Route
@app.route('/dbstatus')
def db_status():
    try:
        # Simple ping to check if DB is responsive
        collection.database.command("ping")
        return jsonify({"status": "MongoDB connection successful ✅"}), 200
    except Exception as e:
        return jsonify({
            "status": "MongoDB connection failed ❌",
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
