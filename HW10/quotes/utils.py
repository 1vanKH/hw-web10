from pymongo import MongoClient
from pymongo.server_api import ServerApi


def get_mongodb():
    client = MongoClient(
    "mongodb+srv://goitlearn:41142058van@cluster0.hq9wumc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    server_api=ServerApi('1'))
    db = client.HW10
    return db


