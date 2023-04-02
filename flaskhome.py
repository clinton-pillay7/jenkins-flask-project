
#roytuts.com - flaskmongo

from flask import Flask
from flask import jsonify, request
import pymongo

clientconn = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = clientconn.rabbit
mycol = mydb.crud

app = Flask(__name__)
@app.route("/")
def hello_world():
	return "<p>hello world</p>"

@app.route("/users")
def users():
	documents = mycol.find()
	response = []
	for document in documents:
		document["_id"] = str(document["_id"])
		response.append(document)
	return jsonify(response)



if __name__ ==  '__main__':
	app.run(host="0.0.0.0", port=5000)