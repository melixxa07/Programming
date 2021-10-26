## Using the same code from The Face Detector App ##

import cv2 
# For random square colors:
from random import randrange

# 3. Load some pre-trained data on face frontals opencv (haar cascade algorithm) << Downloded from Github>>.
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# CascadeClassifier is a funtion to be a classifier (Classify or Detect a Face).

# 4. To Capture Video From Webcam:
webcam = cv2.VideoCapture(0)   
# (0) Will make it take the default webcam.
# A video on the PC can be also added as a str'' in () 

# 5. Iterate forever over frames:
while True:

    # Read the current frame form the webcam:
    succesful_frame_read, frame = webcam.read()   # 'succesful_frame_read' appears when is True or it worked.


    # 5.1. Must convert the image to grayscale (that's how it works).
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # a) cv2.COLOR_BGR2GRAY: Gray scale.
    # b) cv2.COLOR_BGR2RGB: Blue scale.
    # c) cv2.COLOR_RGB2HSV: So much color scale.

    # 5.2. Detect Faces:   << Using the pre-trained data imported to detect multiscale from the gay-scaled video >>.
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    # detectMultiScale detects objects of different sizes in the video. The detected objects are returned as a list of rectangles.

    # 5.3. Draw rectangles around the faces:
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (300,255,0), 3)
    # Original Image, Coordinates of the two corners on the rectangle, Color of the rectangle, Thinckness of the rectangle.
    # a. (300,255,300): White
    # b. (300,255,0): Cyan
    # c. (0,255,0): Green 
    # d. (0,0,255): Red
    # e. ...Explore...
    # f. To make a random color for each person: (randrange(128),randrange(128),randrange(128))  << Color can change between a range of numbers >>

    # 5.4. To display the video with the faces:
    cv2.imshow('Amazing Face Detector Made By Me', frame)
    cv2.waitKey(1)
    # The waitKey() command: When you press any key, the image will quit. 
    # With the number 1 it will wait for that amount of miliseconds to automaticly hit the key for yourself, so it won't look freezed.



    # Stop if Q key is pressed
    #if key==81 or key==113:
    # key==81>>Q and key==113>>q
        #break

# Release the VideoCapture object
##webcam.release()