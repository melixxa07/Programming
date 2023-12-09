import cv2
import numpy as np



#&                                                    -- JOIN IMAGES TOGETHER -- 

img = cv2.imread('D:\Escritorio\Programming\Open CV\Media\Me.jpg')
img = cv2.resize(img, (491,426))  

#---
#& The First way (This doesn't work if the images have a different number of channels and if they have different size):
# We are going to stack it:
# ~ Horizontal stack function:
imgHor = np.hstack((img, img))   # This only work if the images have the same number of channels

# ~ Vertical stack function:
imgVer =  np.vstack((img, img))
#---



#& The final way (The images can be scaled and can have different channels):

#^ This works with this function:

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


# Let's get other images:
img2 = cv2.imread('Open CV/Media/Love.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Let's try the function:
imgStack = stackImages(0.7, ([img, imgGray, img], [img2, img, img2])) # If I have 3 columns in the first row, then I have to have 3 columns in the second row


cv2.imshow('Stack Images', imgStack)
#cv2.imshow('Horizontal', imgHor)
#cv2.imshow('Vertical', imgVer)
cv2.waitKey(0)