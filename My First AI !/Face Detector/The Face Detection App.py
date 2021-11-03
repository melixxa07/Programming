# 1. Install OpenCV.

# 2. Import OpenCV.
import cv2 
# For random square colors:
from random import randrange

# 3. Load some pre-trained data on face frontals opencv (haar cascade algorithm) << Downloaded from Github >>.
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# CascadeClassifier is a funtion to be a classifier (Classify or Detect a Face).

# 4. Choose/Import an image to detect faces in:
img=cv2.imread('D:\Escritorio\Programming\My First AI !\Face Detector\JPM2.jpeg')
# In this case I had to add the whole path so it could find it.

# 4.1 Must convert the image to grayscale (that's how it works).
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# a) cv2.COLOR_BGR2GRAY: Gray scale.
# b) cv2.COLOR_BGR2RGB: Blue scale.
# c) cv2.COLOR_RGB2HSV: So much color scale.

# 5. Detect Faces:   << Using the pre-trained data imported to detect multiscale from the gray-scaled image >>.
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
# detectMultiScale detects objects of different sizes in the input image. The detected objects are returned as a list of rectangles.

print(face_coordinates)
# This prints the location of face with square/rectangle coordinates of the face detector.

# 6. Draw rectangles around the faces:
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (300,255,0), 3)
# Original Image, Coordinates of the two corners on the rectangle, Color of the rectangle, Thinckness of the rectangle.
# a. (300,255,300): White
# b. (300,255,0): Cyan
# c. (0,255,0): Green 
# d. (0,0,255): Red
# e. ...Explore...
# f. (0,0,0): Black
# g. To make a random color for each person: (randrange(128),randrange(128),randrange(128))  << Color can change between a range of numbers >>

# 7. To display the image with the faces:
cv2.imshow('Amazing Face Detector', img)
# The first string is of the name of the window that will show up and the other string is the variable of the image you want to see.

cv2.waitKey()
# The waitKey() command: When you press any key, the image will quit.
# The waitKey() is necessary in OpenCV to display something.


print('Code Completed')