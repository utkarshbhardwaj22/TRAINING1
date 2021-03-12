"""
JASON -> It is the type of dictonary in the form of a string
"""
import json

employee= {"Name": "utkarsh",
           "age" : 21,
           "status": "unemployeed"}

print(employee,type(employee))
print()

data_json = json.dumps(employee) # conversion of ditionary into json
print(data_json,type(data_json))
print()

data_dict = json.loads(data_json) # conversion of json into dictionary 
print(data_dict, type(data_dict))