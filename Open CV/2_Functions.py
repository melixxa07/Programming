import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('D:\Escritorio\Programming\Open CV\Media\Me.jpg')
kernel = np.ones((5, 5), np.uint8)  # Define a matrix 5x5 fulled of number 1 | The type of the object => np.uint8 => Values can range from 0 to 255


#& Resizing The Image:

# Let's see the amount shape/size of the matrix (image) => (Height=852, Width=982)
#print('Image Width is',img.shape[1])
#print('Image Height is',img.shape[0])
img = cv2.resize(img, (491,426))    # We cut the size in half


#& Converting into Gray Scale color:

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray Me', imgGray)
#cv2.waitKey(0)


#& To Blur the image:

imgBlur = cv2.GaussianBlur(imgGray, (11,11), 0)   # This has to be odd numbers


#& Silhouette Edge Detector:

imgCanny = cv2.Canny(img, 105, 150)  # This numbers are called "Treshold" and by changing them the number of edges is going to be modified
# The higher the number, the fewer edges it will have (just by changing one of the two numbers)

#~ Increase the thickness of the edge:

imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)   # The N° of iterations define the thinkess of the edge (> iteration's N° > thickness)
# This also work for the gay scaled image

#~ Decrease the thickness of the edge:

imgEroded = cv2.erode(imgDialation, kernel, iterations=1)    # The N° of iterations define the thinness of the edge (> iteration's N° > thinness)
# This also work for the gay scaled image


cv2.imshow('Gray Img', imgGray)
cv2.imshow('Blur Img', imgBlur)
cv2.imshow('Canny Img', imgCanny)
cv2.imshow('Dialation Img', imgDialation)
cv2.imshow('Eroded Img', imgEroded)
cv2.waitKey(0)




# TODO: 21:00
