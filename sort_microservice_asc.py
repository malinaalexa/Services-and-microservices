from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/sort', methods=['POST'])
def sort_vector():
    data = request.get_json()
    vector = data.get('vector')
    if vector:
        maximum = max(vector)
        return jsonify({'result': maximum})
    else:
        return jsonify({'error': 'Invalid data'}), 400

if __name__ == '__main__':
    app.run(port=5000)
