import pymongo


client = pymongo.MongoClient("mongodb+srv://dbuser:utkarsh11@cluster0.bfzll.mongodb.net/dbuser?retryWrites=true&w=majority")
db = client['dbuser']
collection = db['student']
data = {"name": "piyush", "email": "bhard96piyush@gmail.com", "phone": 7885214752}
document = collection.insert_one(data)
print("Documented Inserted")

