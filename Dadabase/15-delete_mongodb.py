from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://admin:root@localhost:27017/my_db?authSource=admin")


mydb = client.obcblog
mycol = mydb.posts

myquery = {"category": "Data Analysis"}

x = mycol.delete_one(myquery)

print(f"{x.deleted_count} documento excluído")