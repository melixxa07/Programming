import cv2
import numpy as np

#?-----------------------------
#?                LET'S IMPORT THE JOINING IMAGES CODE SO WE CAN VISUALIZE THE WINDOWS OR DISPLAYED IMAGES MORE COMFORTABLY:

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
#?-----------------------------




#&                                                      -- COLOR DETECTION-- 

# We are going to detect this car color
img = cv2.imread('Open CV/Media/Car.jpg')
#print(np.shape(img))
img = cv2.resize(img, (853, 480))

#& 1. Frist, We are going to convert into HSV space:  (No linear space transformation of the color RGB) - Hue, Saturation, Value = Tonalidad, Saturación, Valor
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


#& 2. Now we need to define some color values ranges in which we want our color to be so. In this way by detecting or being in this range, our code is going to wrap it
# We difine hue, the saturation and the value limits 
# For this, we need to use track bars that will help us to play around with the values in real time, so we can find de minimum, maximum and optimal values of our color

#~ 2.1. We create a new Window for the Track bar:
def empty(x):
    pass

cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 250)
cv2.createTrackbar('Hue Min', 'TrackBars', 97, 179, empty)  
# cv2.createTrackbar(Name = Value we are going to change using the trackbar, Window we put this trackbar on, current/initial value, maximum value = 179, function that will run everytime something changes in the trackbar)
# The function 'empty' must be defined before as we can see above

# We need 6 trackbars in total for HSV (max and min hue, saturation and value):
cv2.createTrackbar('Hue Max', 'TrackBars', 110, 179, empty)  # We put the initial as the maximum value in the maximum tracknbar
cv2.createTrackbar('Sat Min', 'TrackBars', 36, 255, empty) 
cv2.createTrackbar('Sat Max', 'TrackBars', 255, 255, empty)  # We put the initial as the maximum value in the maximum
cv2.createTrackbar('Val Min', 'TrackBars', 91, 255, empty) 
cv2.createTrackbar('Val Max', 'TrackBars', 255, 255, empty)  # We put the initial as the maximum value in the maximum

#~ 2.2. We are going to read this trackbar values so we can apply it on our image:
# We need to run this like a loop, so we create a while loop:
while True:
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBars')  # We get the tackbar position of hue min
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBars')  # We get the tackbar position of hue max
    s_min = cv2.getTrackbarPos('Sat Min', 'TrackBars')  # We get the tackbar position of saturation min
    s_max = cv2.getTrackbarPos('Sat Max', 'TrackBars')  # We get the tackbar position of saturation max
    v_min = cv2.getTrackbarPos('Val Min', 'TrackBars')  # We get the tackbar position of value min
    v_max = cv2.getTrackbarPos('Val Max', 'TrackBars')  # We get the tackbar position of value max
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    #~ 2.3 We are going to use this values to filter out our image so we can get that particular color in that range:
    lower = np.array([h_min, s_min, v_min])  # Minimum values
    upper = np.array([h_max, s_max, v_max])  # Maximum values
    
    mask = cv2.inRange(imgHSV, lower, upper)  # Lower limit = Minimum, Upper limit= Maximum
    # We create a mask that is in the range of this colors
    # We difne the lower and upper limit above
    #^ WE WANT TO KEEP ALL THE COLORS WE WANT/NEED IN WHITE AND THE COLORS WE DON'T WANT/NEED IN BLACK
    
    
    #& 3. Now, we need to create a new image with the color that's located in the white zone. (we create an image using the mask)
    imgResult = cv2.bitwise_and(img, img, mask = mask)  # Add two images together to create a new image
    # (Our image, the first image to mix, the second image to mix)


    # cv2.imshow('Car', img)
    # cv2.imshow('HSV Car', imgHSV)
    # cv2.imshow('Mask', mask)
    # cv2.imshow('Result', imgResult)
    # cv2.waitKey(1)  # One because we want it to read it every millisecond
    
    # Let's put all the images together using the function above:
    StackedImages = stackImages(0.5, ([img, imgHSV], [mask, imgResult]))
    cv2.imshow('Stacked Images', StackedImages)
    cv2.waitKey(1)  # The code runs every millisecond so every change is shown simultaneously
    
    
    
    

