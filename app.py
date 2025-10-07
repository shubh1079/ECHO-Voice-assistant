from flask import Flask, jsonify
import subprocess

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
        subprocess.Popen(['python', 'main.py'])
        return jsonify({"message": "ECHO started"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
