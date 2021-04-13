import cv2
import numpy as np

image = cv2.imread("windows.jpg", 1)
print(image)
print()

rotated_image = np.rot90(image)
print(rotated_image)

cv2.imshow("rotated image",rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()