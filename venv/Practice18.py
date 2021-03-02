employee = {
    "eid": 101,
    "name": "utkarsh bhardwaj",
    "Designation": "Team leader",
    "salary": 80000,
    "technology": "python"
}

print(employee,type(employee))
print(min(employee))  #basis on ACSII value
print(max(employee))
print(len(employee))

employee["salary"]=56789

del employee["technology"]

print("^^^^^^^^^^^^")
print(employee)

keys= employee.keys()
print(keys)     # print the keys of dictionary keys

values= employee.values()
print(values)


# Sclicing only work in indexing