"""
Data science:
    numpy
    matplotlib
    seaborn
    pandas
    scikit -> Machine learning
"""
import numpy as np

print(np.__version__)

numbers = [10,20,30]
print(numbers, type(numbers))
print()

array1 = np.array([10,20,30,40])
print(array1, type(array1))

print()

num1= {10,20,30,40}
array2 = np.array(num1)
print(array2, type(array2))

print()

num2 = { "name": "Utkarsh", "email": "utkarsh2000bhard@gmail.com", "phone": 7888327841}
array3 = np.array(num2)
print(array3, type(array3))

print()

num3 = (10,20,30,40)
array4 = np.array(num3)
print(array4, type(array4))

print()

num4 = "utkarsh"
print(num4,type(num4))
array5 = np.array(num4)
print(array5, type(array5))
print(np.size(array4))