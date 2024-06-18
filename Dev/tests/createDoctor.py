import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
# Access the "Hospital" database
db = client["Hospital"]
# Access the "doctors" collection
collection = db["doctors"]

# Define the data to insert
data = [
    {"name": "A. Harischandra", "email":"harischandra@gmail.com" , "occupation": "FD", "password":"harischandra123"},
    {"name": "R. Bandaranayake", "email":"bandaranayake@gmail.com" , "occupation": "EET", "password":"bandaranayake123"},
    {"name": "N. K. Jayathilake", "email":"jayathilaka@gmail.com" ,"occupation": "OS", "password":"jayathilake123"},
    {"name": "H. Wells","email":"wells@gmail.com" , "occupation": "G", "password":"wells123"}
]

# Insert the data into the collection
collection.insert_many(data)
