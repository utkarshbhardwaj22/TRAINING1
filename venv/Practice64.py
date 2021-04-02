import numpy as np

array1 = np.array([10,20,30]) #ndarray -> 1D
array2 = np.array([[10,20,30],[40,50,60],[70,80,90]]) #ndarray of ndarray -> 2D
array3 = np.array([[10,20],[30,40,50,60,70],[70,80,90,40]]) #ndarray of lists -> 1D

print(array1)
print(array2)
print(array3)

print()

print("Shape of array1: ",array1.shape)
print("Shape of array2: ",array2.shape)
print("Shape of array3: ",array3.shape)