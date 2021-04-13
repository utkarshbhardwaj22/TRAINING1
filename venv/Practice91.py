import cv2

image = cv2.imread("windows.jpg", 1)
print(image)

resized_image = cv2.resize(image,(image.shape[0]//3, image.shape[1]//3))
print(resized_image)

cv2.imshow("Resized image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()