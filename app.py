from flask import Flask, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to ECHO Voice Assistant API",
        "status": "Running Successfully!"
    })

@app.route('/start', methods=['GET'])
def start_echo():
    try:
        # Run the ECHO assistant (for local or debug environments)
        subprocess.Popen(['python', 'main.py'])
        return jsonify({"message": "ECHO started"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Use Railway-assigned PORT or fallback to 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
