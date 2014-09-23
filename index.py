from bottle import route, get,post,request,run, template,response

import pymongo
import json
from bson import BSON,Code
from bson import json_util
from bson.objectid import ObjectId 

client = pymongo.MongoClient("localhost",27017)
test = "admin"
db = client[test]
print db.name
 
@get('/<database>/<collection>')
def index(database,collection):
	
	response.content_type = 'application/json; charset=utf8'
	doc = client[database][collection].find()
	result = json.dumps(list(doc), sort_keys=True, indent=4, default=json_util.default)
	return result

@get('/<database>/<collection>/<id>')
def index(database,collection,id):

	response.content_type = 'application/json; charset=utf8'
 	doc = client[database][collection].find_one({'_id': ObjectId(id)})
	result = json.dumps(doc, sort_keys=True, indent=4, default=json_util.default)
	return result
 

 
run(host='localhost', port=8080)