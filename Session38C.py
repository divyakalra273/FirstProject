import cv2
import numpy as np
image=cv2.imread("download.jpg",1)#0 for black and white
print(image)
rotatedImage=np.rot90(image)

# cv2.imshow("Image",image)
cv2.imshow("Image",rotatedImage)

#cv2.waitKey(2000)

cv2.waitKey(0) #Take any keyboard input then quit
cv2.destroyAllWindows()