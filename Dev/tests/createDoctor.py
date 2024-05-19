import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
# Access the "Hospital" database
db = client["Hospital"]
# Access the "doctors" collection
collection = db["doctors"]

# Define the data to insert
data = [
    {"name": "A. Harischandra", "occupation": "FD"},
    {"name": "R. Bandaranayake", "occupation": "EET"},
    {"name": "N. K. Jayathilake", "occupation": "OS"},
    {"name": "H. Wells", "occupation": "G"}
]

# Insert the data into the collection
collection.insert_many(data)
