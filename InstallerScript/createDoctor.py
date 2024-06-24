import pymongo

print("Creating Doctor Accounts...")
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Hospital"]
collection = db["doctors"]
data = [
    {"name": "A. Harischandra", "email":"harischandra@gmail.com" , "occupation": "FD", "password":"harischandra123"},
    {"name": "R. Bandaranayake", "email":"bandaranayake@gmail.com" , "occupation": "EET", "password":"bandaranayake123"},
    {"name": "N. K. Jayathilake", "email":"jayathilaka@gmail.com" ,"occupation": "OS", "password":"jayathilake123"},
    {"name": "H. Wells","email":"wells@gmail.com" , "occupation": "G", "password":"wells123"}
]
collection.insert_many(data)
