# Arthmetic operations on numpy array

import numpy as np

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

B = np.array([[11,22,33],
              [44,55,66],
              [77,88,99]])

sum = A+B
print("SUM: ",sum)
print()

diff = A-B
print("DIFFERENCE: ", diff)
print()

mul = A*B
print("MULTIPLICATION: ", mul)
print()

div = A/B
print("DIVISION: ", div)
print()

X= A.T
print("TRANSPOSE:\n ",X)
