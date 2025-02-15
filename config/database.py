import urllib.parse
from pymongo import MongoClient

username = "OmkarM"
password = "Omk@r2176"

encoded_password = urllib.parse.quote_plus(password)
uri = f"mongodb+srv://{username}:{encoded_password}@cluster0.pztjk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)
db = client.todo_db
collection_name = db["todo_collection"]
