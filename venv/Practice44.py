import pymongo
print(pymongo.__version__)

#Created connection to MongoDB
url = "mongodb+srv://dbUtk:utkarsh%4012@cluster0.tgh14.mongodb.net/utkarsh?retryWrites=true&w=majority"
encoded_url = "mongodb%2Bsrv%3A%2F%2FdbUtk%3Autkarsh%4012%40cluster0.tgh14.mongodb.net%2Futkarsh%3FretryWrites%3Dtrue%26w%3Dmajority.0"
client = pymongo.MongoClient(encoded_url)

# Obtain reference to the database
# db = client.utkarsh
db = client['utkarsh']

#listing the collections
#collections = db.list_collection_names()
#print(collections)

collection = db["students"]
student = {"name": "piyush", "rollno": 14113014, "class": "D4PEA"}
document = collection.insert_one(student)
print("Documented Inserted: ",document.__inserted_id)

