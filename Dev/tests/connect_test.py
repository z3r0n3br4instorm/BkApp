import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a database named 'test'
db = client["test"]

# Create a collection (table) named 'example_table'
example_table = db["example_table"]

# Example values
data = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Alice", "age": 25, "city": "Los Angeles"},
    {"name": "Bob", "age": 35, "city": "Chicago"}
]

# Insert example values into the collection
example_table.insert_many(data)

# Display the inserted data
print("Data in example_table:")
for document in example_table.find():
    print(document)
