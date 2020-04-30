import cv2
import numpy as np
image=cv2.imread("download.jpg",1)#0 for black and white
print("===Original Image===")
print(image)

print("===Original Image Shape===")
shape=image.shape
print(shape)
print("===Resized Image Shape===")
resizedImage=cv2.resize(image,(shape[1]//2,shape[0]//2))
resizedShape=resizedImage.shape
print(resizedShape)
cv2.waitKey(0) #Take any keyboard input then quit
cv2.destroyAllWindows()