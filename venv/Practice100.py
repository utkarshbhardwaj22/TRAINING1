import matplotlib.pyplot as plt
from sklearn import datasets

digits = datasets.load_digits()
print(digits)

print()
print("FEATURES")
print(digits['images'])
print()
print("LABELS")
print(digits['target'])

print("Image at 0th Index")
print(digits['images'][0])
print("Image label at 0th index")
print(digits['target'][0])
print()

print("Image at 9th Index")
print(digits['images'][9])
print("Image label at 9th index")
print(digits['target'][9])
print()

print("Image at 99th Index")
print(digits['images'][99])
print("Image label at 99th index")
print(digits['target'][99])
print()
"""
plt.subplot(2,4,1)
plt.imshow(digits['images'][0], cmap=plt.cm.gray_r)

plt.subplot(2,4,2)
plt.imshow(digits['images'][1], cmap=plt.cm.gray_r)

plt.subplot(2,4,3)
plt.imshow(digits['images'][2], cmap=plt.cm.gray_r)

plt.subplot(2,4,4)
plt.imshow(digits['images'][3], cmap=plt.cm.gray_r)
"""

position = 1
for i in range(8):
    plt.subplot(2, 4, position)
    plt.imshow(digits['images'][position], cmap=plt.cm.gray_r)
    position +=1

plt.show()