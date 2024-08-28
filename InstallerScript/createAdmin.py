import pymongo

print("Creating Admin Accounts...")
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Hospital"]
collection = db["admin"]
data = [
    {"name": "admin", "email":"admin@gmail.com" , "password":"admin123"}
]
collection.insert_many(data)
