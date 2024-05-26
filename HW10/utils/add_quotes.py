import json
from bson import ObjectId
from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://goitlearn:41142058van@cluster0.hq9wumc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    server_api=ServerApi('1'))

db = client.HW

with open('quotes.json', 'r', encoding='utf-8') as f:
    quotes = json.load(f)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })
    