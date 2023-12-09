import cv2
import numpy as np

'''
# ? Let's work with an image with perspective:
img = cv2.imread('D:\Escritorio\Programming\Open CV\Media\Perspective_Image.jpg')
#print(np.shape(img))
img = cv2.resize(img, [764, 430])



#&                                                  -- WRAP PERSPECTIVE --


#? Let's take the NASA drawing:

width, height = 350, 350  # Size of the image that is going to show the window

# Define our four corner points of the image:  (I TOOK THIS POINTS FROM PAINT)
pts1 = np.float32([[142, 164], [275, 177], [134, 277], [286,278]])
# Let's define what kind of points are each of this:
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])
# Let's define the variables "width" and "height" above.

# Now, we get our transformation matrix that will be require for the perspective
matrix = cv2.getPerspectiveTransform(pts1, pts2)
# The output image: 
imgOutput = cv2.warpPerspective(img, matrix, (width, height))   # (image, matrix, (width, height))



#? Let's take the UTSA:

width2, height2 = 300, 215

# Define our four corner points of the image:  (I TOOK THIS POINTS FROM PAINT)
pts3 = np.float32([[364, 242], [435, 245], [368, 281], [447,284]])
# Let's define what kind of points are each of this:
pts4 = np.float32([[0,0], [width2, 0], [0, height2], [width2, height2]])
# Let's define the variables "width" and "height" above.

# Now, we get our transformation matrix that will be require for the perspective
matrix2 = cv2.getPerspectiveTransform(pts3, pts4)
# The output image: 
imgOutput2 = cv2.warpPerspective(img, matrix2, (width2, height2))   # (image, matrix, (width, height))



cv2.imshow('Image', img)
cv2.imshow('Image with Perspective (NASA)', imgOutput)
cv2.imshow('Image with Perspective (UTSA)', imgOutput2)
cv2.waitKey(0)

'''



#^ Let's try this with another picture <3:

img = cv2.imread('D:\Escritorio\Programming\Open CV\Media\Love.jpg')
#print(np.shape(img))
img = cv2.resize(img, [406, 722])


width, height = 600, 900
# Define the points:
pts1 = np.float32([[120,234], [277,216], [86,511], [246,559]])
# Define what these points are:
pts2 = np.float32([[0, 0], [width ,0], [0, height], [width, height]])
# Let's define width and height above

# Now, we get our transformation matrix that will be require for the perspective:
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))


cv2.imshow('My baby and I', img)
cv2.imshow('Drawing', imgOutput)
cv2.waitKey(0)

