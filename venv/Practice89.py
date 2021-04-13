import cv2

image = cv2.imread("windows.jpg", 1)
print(image)
print()
print(type(image))
print()
print(image.shape)
print()
print(image[0])
print()
print(len(image))