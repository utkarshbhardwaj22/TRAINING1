import cv2
import time

video = cv2.VideoCapture(0)

check, frame = video.read()

print("CHECK\n", check)
print()
print("Frame\n", frame)

time.sleep(5)

cv2.imshow("hehe", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
