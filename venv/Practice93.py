import cv2

video = cv2.VideoCapture(0)

frame_count = 0

while True:
    check, frame = video.read()
    frame_count +=1
    print(frame)
    cv2.imshow("framecount{}".format(frame_count), frame)
    key = cv2.waitKey(1)

    cv2.imwrite("hello.jpg", frame)

    if key == ord('q'):
        break
print("framecount: ", frame_count)
cv2.destroyAllWindows()
