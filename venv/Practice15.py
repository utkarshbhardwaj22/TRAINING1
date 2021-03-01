"""
Conversions
"""

numbers1=(10,20,30,20,40)
print(numbers1,type(numbers1))
print("^^^^^^^^^^^^^^^^^^")

numbers2=list(numbers1)
print(numbers2,type(numbers2))
print("^^^^^^^^^^^^^^^^^^^")

numbers3= set(numbers1)
print(numbers3,type(numbers3))
print("^^^^^^^^^^^^^^^^^^^")

numbers4= str(numbers1)
print(numbers4,type(numbers4))
print("^^^^^^^^^^^^^^^^^^^")
print(numbers4[5])
print(numbers4[::-1])
print()


name="utkarsh"
print(name[::-1])
