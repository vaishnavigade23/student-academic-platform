from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return jsonify({
            "message": "Student Academic Management Platform is running!"
        })

    @app.route("/health")
    def health():
        return jsonify({"status": "healthy"}), 200

    return app
