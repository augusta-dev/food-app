import pymongo
from pymongo import MongoClient

cluster = MongoClient(("mongodb+srv://augustandev:<password>@meals.mg1iwwn.mongodb.net/?retryWrites=true&w=majority&appName=meals"))

# client=pymongo.MongoClient('mongodb://192.168.3.251:8000/')

# mydb=client['restaurant-api']

# meals = client['meals']

# print(meals)


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
uri = os.environ.get('MONGO_URI')
print(uri)
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)