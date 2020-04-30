import cv2
print (cv2.__version__)

image=cv2.imread("download.jpg",1)
print("==Image==")
print(image)

print("===Image Shape===")
print(image.shape)

print("Image 0th position")
print(image.shape[0])
print(image[0])

