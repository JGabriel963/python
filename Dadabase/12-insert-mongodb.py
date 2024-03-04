from pymongo import MongoClient

client = MongoClient("mongodb://admin:root@localhost:27017/my_db?authSource=admin")

mydb = client.obcblog
mycol = mydb.posts

post1 = {
    "title": "Web Scraping",
    "category": "Automação",
    "author": {
        "name": "Fulano",
        "email": "fulano@mail.com"
    }
}


result = mycol.insert_one(post1)
print("Documento incluído com sucesso")