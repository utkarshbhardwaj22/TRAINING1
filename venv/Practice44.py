import pymongo
print(pymongo.__version__)

#Created connection to MongoDB
url = "mongodb://dbUtk:utkarsh@cluster0-shard-00-02.tgh14.mongodb.net:27017,cluster0-shard-00-01.tgh14.mongodb.net:27017,cluster0-shard-00-00.tgh14.mongodb.net:27017/utkarsh?ssl=true&replicaSet=atlas-f8rvp5-shard-0&authSource=admin&retryWrites=true&w=majority"
client = pymongo.MongoClient(url)
db = client['utkarsh']

#listing the collections
#collections = db.list_collection_names()
#print(collections)

collection = db["students"]
student = {"name": "piyush", "email": "bhard96piyush@gmail.com", "rollno": 1706902}
document = collection.insert_one(student)
print("Documented Inserted: ",document.__inserted_id)

