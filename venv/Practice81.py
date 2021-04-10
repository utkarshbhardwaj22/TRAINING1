import pandas as pd

numbers1 = [10,20,30,40,50]
numbers2 = [11,22,33,44,55]

employee1 = {"name": "utkarsh", "age": 21, "salary": 100000, "designation":"CEO(GOOGLE)"}
employee2 = {"name": "dinesh", "age": 20, "salary": 35000, "designation":"Security Enfgineer"}
employee3 = {"name": "deepak", "age": 22, "salary": 30000, "designation":"Lab Assistant"}
employee4 = {"name": "harpreet", "age": 21, "salary": 20000, "designation":"Chaprasi"}
employee5 = {"name": "rahul", "age": 22, "salary": 45000, "designation":"AFCAT Trainee"}

table1 = pd.DataFrame([numbers1, numbers2])
table2 = pd.DataFrame([employee1, employee2, employee3, employee4, employee5])

print(table1)
print()
print(table2)
#del table1[1]
#print(table1)

t = table1.drop(0,axis=1)
print(t)