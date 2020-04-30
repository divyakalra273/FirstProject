import cv2,time

video=cv2.VideoCapture(0)
check,frame=video.read()
print("===Check===")
print(check)
print("===Frame===")
print(frame)

time.sleep(5)

video.release()
cv2.imshow("My Frame",frame)

cv2.destroyAllWindows()