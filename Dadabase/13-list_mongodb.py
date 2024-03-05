from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://admin:root@localhost:27017/my_db?authSource=admin")

mydb = client.obcblog
mycol = mydb.posts

result = mycol.find()
for r in result:
    pprint(r['author'])