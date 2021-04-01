import pymongo

class DB:

    def __init__(self):
        url="mongodb+srv://dbUtk:utkarsh@cluster0.tgh14.mongodb.net/utkarsh?retryWrites=true&w=majority"
        encoded_url = "mongodb%2Bsrv%3A%2F%2FdbUtk%3Autkarsh%40cluster0.tgh14.mongodb.net%2Futkarsh%3FretryWrites%3Dtrue%26w%3Dmajority"
        client = pymongo.MongoClient(url)
        db = client['utkarsh']

        collection = db['students']
        student = {"name": "piyush", "email": "bhard96piyush@gmail.com", "rollno": 1706902}
        document = collection.insert_one(student)
        print("Documented Inserted: ", document.__inserted_id)
