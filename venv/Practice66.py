import numpy as np
import time

t1 = time.time()
A = list(range(1,11))
print(A)
t2 = time.time()

t3 = time.time()
B = np.arange(1,11)
print(B)
t4 = time.time()

print()
print("Time for List: ",t2-t1)
print()
print("Time for Numpy: ",t4-t3)

print("SLICING")
#[1,2,3,4,5,6,7,8,9,10]
X = B[1:7:3]     # Step Slicing
Y = B[2:5:2]
print(X)
print(Y)

