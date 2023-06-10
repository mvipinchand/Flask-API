import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


def make_POST_request(port, service, payload):
    url = 'http://localhost:port/service'.replace('port', port).replace('service', service)
    return requests.post(url, json=payload)

@app.route("/db-app", methods=['GET', 'POST'])
def all_app_requests():
    if request.method == 'POST':
        request_body = request.json
        if request_body['type'].lower() == 'sql':
            response = make_POST_request('9001', 'get-data', request_body)
            return response.json()
        if request_body['type'].lower() == 'mongodb':
            response = make_POST_request('9002', 'get-data', request_body)
            return response.json()


#Gateway service running on port 9000
if(__name__) == '__main__':
    app.run(host='localhost', port=9000, debug=True)