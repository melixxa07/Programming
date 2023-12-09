import cv2
import numpy as np

img = cv2.imread('D:\Escritorio\Programming\Open CV\Media\Me.jpg')

# Let's check the shape of our image
print(np.shape(img))


#& Resizing The Image:

imgResized = cv2.resize(img, (400,350))


#& Cropping the image:

# We don't need the open cv library, but we can work with functions
imgCropped = img[150:500, 326:700]   # img[height, width]



cv2.imshow('Me', img)
cv2.imshow('Me Resized', imgResized)
cv2.imshow('Me Cropped', imgCropped)
cv2.waitKey(0)