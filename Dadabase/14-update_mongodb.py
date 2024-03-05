from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://admin:root@localhost:27017/my_db?authSource=admin")

mydb = client.obcblog
mycol = mydb.posts

old_value = { "category": "Data Analysis" }
new_value = {"$set": { "category": "Backend" }}

mycol.update_one(old_value, new_value)

for x in mycol.find():
    pprint(x)