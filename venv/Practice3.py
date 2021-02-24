"""
Multi value containers
1. Tuple
2. Set
3. List
4. Dictionary
"""

"""
==================================================
Tuple

names= ("utkarsh", "piyush","ekansh","avisha")

print("Names of person:",names)
print("type of names:", type(names))

print(names[3])
print("Number of names:", len(names))

#del names[0]
# Tuples are IMMUTABLE (Read only operation)
# tuples are used where data is fixed
=========================================
"""


"""
==============================
List
list is mutable
it suppoerts duplicates

names= ["utkarsh", "piyush","ekansh","avisha"]
print("Names of person:",names)
print("type of names:", type(names))

print()

names.append("Anvay")


del names[1]
print(names)
========================================
"""

"""
Set

"""
names= {"utkarsh", "piyush","ekansh","avisha"}
print("Names:",names)

names.add("Anvay")
names.add("Dev")
names.add("utkarsh")
print("Names:",names)
print("Length:",type(names))
