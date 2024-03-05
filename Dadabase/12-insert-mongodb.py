from pymongo import MongoClient

client = MongoClient("mongodb://admin:root@localhost:27017/my_db?authSource=admin")

mydb = client.obcblog
mycol = mydb.posts

post1 = {
    "title": "FastApi",
    "category": "Data Analysis",
    "author": {
        "name": "Joel",
        "email": "joel@mail.com"
    }
}


result = mycol.insert_one(post1)
print("Documento incluído com sucesso")