Drivers = [
    {"name": "Utkarsh",
     "status": 1,
     "distance": 16
     },

    {"name": "Dinesh",
     "status": 0,
     "distance": 15
     },
    {"name": "Harpreet",
     "status": 1,
     "distance": 3
     },
    {"name": "Deepak",
     "status": 1,
     "distance": 5
     },
]

Customers= {"name": "Abhishek lalotra",
     "phone": 7888327841,
     "email": "abhishek11@gmail.com",
     "distance": 5}


for i in range(len(Drivers)):
    if Drivers[i]["status"] !=1:
        continue
    if Drivers[i]["distance"] > Customers["distance"]:
        continue

    print("Driver Found",Drivers[i]["name"])

    print("Dear", Customers["name"],"your cab is booked: SMS send on", Customers["phone"])
    break