import numpy as np

mat = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("Matrix: ")
print(mat)
print(mat.shape)
print()

Y = np.empty_like(mat)
print("Y: ")
print(Y)
print(Y.shape)

print(len(mat))
print()

for i in range(len(mat)):
    print(mat[i-i])

met = np.array([
    [1],
    [3],
    [5]
])
print()
print("Shape of mat: ", mat.shape)
print("Shape of met: ", met.shape)
print()
Z = met * mat
print(Z, Z.shape)