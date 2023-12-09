import cv2
import numpy as np


#&                                            -- HOW TO DRAW SHAPES AND TEXTS ON IMAGES --

#^  Note: Zero means Black and One means White

# Let's create our matrix full of zeros:
img_Black = np.zeros((512, 512))   # This is a black image of 512x512 pixels (1 channel)

# To add colors to our image we have to add 3 channels (RGB)
img = np.zeros((512, 512, 3), np.uint8) 
#? img[:] = (255, 0, 0)  # This puts the whole image in BLUE color (255,0,0)=>Blue
# To put color to a certain part of the image is img[height=(#:#), width=(#:#)]


 
#&                                                       TO CREATE SHAPES:

#& - To create lines:

cv2.line(img, (0,0), (300,300), (255,230,0), 3)   # cv2.line(img, (start point), (end point), (color), thickness)


#& - To create rectangles:

cv2.rectangle(img, (0,0), (300,300), (0,255,0), 2)

#~ * To create a filled rectangle:

cv2.rectangle(img, (0,0), (100,100), (0,255,0), cv2.FILLED)   # Thickness = FILLED


#& - To create circles:

cv2.circle(img, (100,100), 50, (153, 0, 0), cv2.FILLED)
cv2.circle(img, (100,100), 50, (153, 0, 0), 5)




#&                                                        TO PUT TEXTS:

cv2.putText(img, 'Me <3', (100, 400), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255,230,0), 2)
# cv2.putText(img, Text displayed, Location, Font, Scale, Color, Thickness)


cv2.imshow('Image', img)
cv2.waitKey(0)