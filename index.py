from bottle import route, run, template,response
import pymongo
import json
from bson import BSON,Code
from bson import json_util
from bson.objectid import ObjectId 

client = pymongo.MongoClient("localhost",27017)
test = "admin"
db = client[test]
print db.name
 
@route('/<database>/<collection>')
def index(database,collection):
	
	response.content_type = 'application/json; charset=utf8'
	doc = client[database][collection].find()
	result = json.dumps(list(doc), sort_keys=True, indent=4, default=json_util.default)
	return result

@route('/<database>/<collection>/<id>')
def index(database,collection,id):

	response.content_type = 'application/json; charset=utf8'
 	doc = client[database][collection].find_one({'_id': ObjectId(id)})
	result = json.dumps(doc, sort_keys=True, indent=4, default=json_util.default)
	return result
 
 
run(host='localhost', port=8080)