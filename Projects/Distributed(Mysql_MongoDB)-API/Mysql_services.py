import mysql.connector as conn
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-data',methods=['POST'])
def dbretrival():

    request_body = request.json
    if 'username' in request_body.keys() and 'password' in request_body.keys():
        mydba = conn.connect(host='localhost', user=str(request_body['username']), passwd=str(request_body['password']))
        cursor = mydba.cursor()

        if 'query' in request_body.keys():
            cursor.execute(request_body['query'])
            return jsonify({"data" : str(cursor.fetchall())})


#Mysql app running on port 9001
if(__name__) == '__main__':
    app.run(host='localhost', port=9001, debug=True)



# cursor.execute('show databases')
# print(cursor.fetchall())
# # cursor.execute('show tables')
