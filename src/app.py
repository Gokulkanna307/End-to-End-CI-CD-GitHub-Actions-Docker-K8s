from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello, world! Your app is running on Kubernetes!"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    # Run the app on all interfaces so it can be accessed from the container
    app.run(host="0.0.0.0", port=5000, debug=True)

