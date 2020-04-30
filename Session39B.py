import cv2

video=cv2.VideoCapture(0)
frameCount=0
while(True):

    check,frame=video.read()
    frameCount +=1
    print(frame)
    cv2.imshow("My Video",frame)

    key=cv2.waitKey(1)
    if key==ord('q'):
        break
print("Total Frames Captured",frameCount)
video.release()
cv2.destroyAllWindows()

#Assignment: Use OPENCV API and convert list of frames as video and save it