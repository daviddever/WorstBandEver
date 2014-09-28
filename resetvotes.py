import pymongo

connection = pymongo.Connection()
db = connection['worstbandever']
collection = db['artists']

posts = db.artists
posts.update({}, {'$set': {'votes': 0}}, multi=True)
