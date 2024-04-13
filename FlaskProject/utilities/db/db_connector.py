import os
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# get your uri from .env file
uri = os.environ.get('DB_URI')

# create cluster
cluster = MongoClient(uri, server_api=ServerApi('1'))

# get all dbs and collestions that needed
mydatabase = cluster['mydatabase']
customers_col = mydatabase['customers']


# create all necessary functions
def get_list_of_customers():
    return list(customers_col.find())


def insert_customer(customer_dict):
    customers_col.insert_one(customer_dict)

# ...



from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Sapiravi:Hapoelole1@cluster0.kqvizbt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)