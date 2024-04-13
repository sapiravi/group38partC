#
# from flask import uri
# from pymongo import MongoClient
# from pymongo.server_api import ServerApi
#
# DB_URI = "mongodb+srv://Sapiravi:Hapoelole1@cluster0.kqvizbt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#
#
# cluster = MongoClient(uri, server_api=ServerApi('1'))
# db = cluster.MyWorkoutSchedule
#
# WorkoutDetails_col = db['WorkoutDetails']
# for document in WorkoutDetails_col.find():
#     print(document)
#
# Customers_col = db['Customers']
# for document in Customers_col.find():
#     print(document)
#
# Branch_col = db['Branch']
# for document in Branch_col.find():
#     print(document)
from app import db

# DB_URI = "mongodb+srv://Sapiravi:Hapoelole1@cluster0.kqvizbt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

print("Customers_col")
for document in db.Customers.find():
    print(document)
print()

print("WorkoutDetails_col")
for document in db.WorkoutDetails.find():
    print(document)
print()


print("Branch_col")
for document in db.Branch.find():
    print(document)
print()

print("Workouts_col")
for document in db.Workouts.find():
    print(document)
print()

