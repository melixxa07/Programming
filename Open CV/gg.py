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






#&                                                    -- CONTOURS AND SHAPE DETECTION -- 

img = cv2.imread('D:\Escritorio\Programming\Open CV\Media\Shapes.png')
#print(np.shape(img))
img = cv2.resize(img, (400, 400))


#~ 1. Convert the image into gray scale and find the edges to find the corner points
# We covert the color into gray scale:
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# We apply some blur:
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)  # The higher the value of the sigma (1) the more blur you will get

# We are going to detect the edges:
imgCanny = cv2.Canny(imgBlur, 50, 50)


#~ 2. Create a function to get contours:
# Let's create a copy of the image to draw the contour in it:
imgCopy = img.copy()

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # (img, Retrive the extreme outter contours or corners, to get all the contours we have found)
    
    for cnt in contours:
        #~ Let's calculate the area:
        area = cv2.contourArea(cnt)  # The contour we want to find the area for
        print(area)
        #cv2.drawContours(imgCopy, cnt, -1, (255, 0, 0), 3)    # To draw or add to the image the contour detected more clearly
        # (A copy of the image to draw in it, contours, -1 to draw all the contour, color (blue in this case), thickness)

        # Let's check for the minimum area: To get the minimum treshold/limit for the area so it does not detect any noise
        if area > 500:  # 500 pixels
            
            #~ Let's draw the corners detected in the image:
            cv2.drawContours(imgCopy, cnt, -1, (255, 0, 0), 3)    # To draw or add to the image the contour detected more clearly
            # (A copy of the image to draw in it, contours, -1 to draw all the contour, color (blue in this case), thickness)

             # We print it in the center of the object
            #~ Let's calculate the curve length to aproximate the corners of our shape:
            perimiter = cv2.arcLength(cnt, True)  # True because the shape is closed
            #print(perimiter)
            
            #~ Let's approximate how many corner points we have:
            approx = cv2.approxPolyDP(cnt, 0.02*perimiter, True)  # (cnt, we can play with this, True because is closed)
            print(len(approx))  # This gives us the points of each of them
            
            #^ For those len(approx)=corner points: 3=>Triangle, 4=>Rectangle or square and over or greater than 4=>Circles          
            
            #~ Let's create object corners:
            objCor = len(approx)
            # Now we create a bounding box around our detected object:
            x, y, w, h = cv2.boundingRect(approx)
            
            cv2.rectangle(imgCopy, (x,y), (x+w, y+h), (0,0,255), 2)  # We get bounding boxes on the object we are detecting
            #^ This help us to know what is the height and width of the object and what is the center point of the object
            
            #~ NOW, LET'S CATEGORIZE THIS OBJECTS WHETHER IT IS A RECTANGLE, SQUARE, CIRCLE OR TRIANGLE:
            # For Triangle:
            if objCor == 3: ObjectType = 'Triangle'
            # For Square and Rectangle:
            elif objCor == 4:
                aspRatio = w/float(h) 
                if aspRatio > 0.95 and aspRatio < 1.05: ObjectType = 'Square'
                else: ObjectType = 'Rectangle'
                #^ Square =>  width/height = 1  (same sides dimension)
                #^ Rectangle => width/height != 1  (different sides dimension)
            # For circle:
            elif objCor > 4: ObjectType = 'Circle'
            else: ObjectType = 'None'
            
            # Let's put this on the image to identify which object is a triangle:
            cv2.putText(imgCopy, ObjectType, (x+(w//2)-20, y+(h//2)-20), cv2.FONT_ITALIC, 0.5, (0,0,0), 2)
             # We print it in the center of the object
            

# Let's apply the function:
getContours(imgCanny)

# Let's visualize it all in one window:
imgBlank = np.zeros_like(img)
imgStack = stackImages(0.7, ([img, imgGray, imgBlur], [imgCanny, imgCopy, imgBlank]))
cv2.imshow('Stacked Images', imgStack)
cv2.waitKey(0)

