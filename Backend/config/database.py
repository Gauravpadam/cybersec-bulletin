from pymongo import MongoClient

client = client = MongoClient("mongodb+srv://gauravpadam2:Growisto12ee1122@cluster0.7qcntfh.mongodb.net/")

db = client.artices

collections_name = db["Article_Collection"]

