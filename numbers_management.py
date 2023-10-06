import flask
from flask import Flask, request, jsonify
import requests
import json
import time
from waitress import serve

app = Flask(__name__)

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')
    unique_numbers = set()

    for url in urls:
        try:
            response = requests.get(url, timeout=0.5)  # Timeout set to 500 milliseconds
            if response.status_code == 200:
                data = response.json()
                numbers = data.get('numbers', [])
                unique_numbers.update(numbers)
        except requests.exceptions.RequestException:
            pass  # Ignore URLs that take too long to respond

    sorted_numbers = sorted(unique_numbers)
    return jsonify({'numbers': sorted_numbers})

if __name__ == '__main__':
    #running flask application
    #get_numbers()
    # flask_app=get_numbers()
    # serve(flask_app,host='localhost',port=5500,debug=False,url_scheme='https')
    app.run(host='localhost', port=5500)
