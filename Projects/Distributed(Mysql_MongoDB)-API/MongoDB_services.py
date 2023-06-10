from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

@app.route('/get-data', methods=['GET', 'POST'])
def mongodataretrival():

    request_body = request.json
    if(request.method == 'POST'):
        client = pymongo.MongoClient((str(request_body['connection_string'])), tls=True, tlsAllowInvalidCertificates=True)
        db = client[request_body['db_name']]
        coll = db[request_body['collection_name']]
        return jsonify(str(list(coll.find())))


#MongoDB app running on port 9002
if(__name__) == '__main__':
    app.run(host='localhost', port=9002, debug=True)