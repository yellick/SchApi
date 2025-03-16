from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/check_connection', methods=['GET'])
def check_connection():
    return 'true'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)