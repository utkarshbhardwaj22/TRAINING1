import numpy as np

array1 = np.array([10,20,30,40,50])
print(array1[2])

array1[4] = 499
print(array1)

print(len(array1))

for i in array1:
    print(i)

array2 = np.append(array1, [60,38,45,67,34,56])
print(array2)