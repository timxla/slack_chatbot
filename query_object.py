from tokenize import TokenInfo
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.json_util import dumps, loads

class Query:
    def __init__(self):
        self.client = MongoClient(
            "mongodb+srv://findimage123:findimagecapstone@cluster0.p7r2e.mongodb.net/Cluster0?retryWrites=true&w=majority", 
            server_api=ServerApi('1'))
        self.db = self.client["Instagram"]
        self.collection = self.db["posts"]

    def query_by_class(self, class_name, post_date):
        try:
            cursor = self.collection.find({
                "crawl_date" : { "$eq": post_date },
                "detection" : { "$in": [class_name] }
                }, 
                {"img_url" : 1, "likes" : 1, "insta_id" : 1})
            obj_list = list(cursor)
            obj_list = obj_list[:5]
            return obj_list
        except:
            return False
