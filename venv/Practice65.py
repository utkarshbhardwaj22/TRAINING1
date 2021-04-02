import numpy as np

array1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(array1)
print()
#array2 = array1.reshape(3,2)
#print(array2)
print()
print(array1[[0,1,2],[0,0,1]])