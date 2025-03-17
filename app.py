from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello, World! We are here with good news!"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#Working on some improvements
#We need more routes
