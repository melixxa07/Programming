# Importing Library:
import cv2

# Face and smile classifiers:
face_detector = cv2.CascadeClassifier('D:\Escritorio\Programming\My First AI !\Face Detector\haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('D:\Escritorio\Programming\My First AI !\Smile Detector\haarcascade_smile.xml')  
# A smile it's way harder to detect than a face.

# Grab Webcam feed:
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)    ## cv2.CAP_DSHOW to solve [WARN:0] Error

# Realize a loop so it can show frame by frame (Real Time Webcam)
while True:

    # Read current frame from webcam.
    Succesful_frame_read, frame = webcam.read()

    # If there's an error, abort:
    if not Succesful_frame_read:
        print('Error')
        break

    # Change to grayscale:
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    # Detect a face first:
    face_coordinates = face_detector.detectMultiScale(grayscaled_frame)
    ##smile_coordinates = smile_detector.detectMultiScale(grayscaled_frame, scaleFactor=2, minNeighbors=20)  
    # scaleFactor blur the image for optimization (to make it easy to detect faces).
    # minNeighbors set a number of rectangles (20 in this case) in the area to actually count as a smile.
    
    # Run smile detection within each of those faces:
    for (x, y, w, h) in face_coordinates:
 
        # Draw a rectangle around faces:
         cv2.rectangle(frame, (x, y), (x+w, y+h), (300,255,300), 3)

    # Getting the face frame to use it to detect smiles:
    # Get the sub frame (using the rectangle of the face as an image) << Using numpy N-dimensional array slicing >>
    the_face = frame[y:y+h, x:x+w]   # We are selecting the section of the image. [This works because OpenCV is build in numpy]
        
    # Change to graysacle:
    grayscaled_face = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

    # Smile detector for the detected face:
    smile_coordinates = smile_detector.detectMultiScale(grayscaled_face, scaleFactor=2, minNeighbors=20)   

    # Find all smiles in individual faces:
    #for (x_, y_, w_, h_) in smile_coordinates:   
        # Draw all rectangles around the smile:
        #cv2.rectangle(the_face, (x_, y_), (x_ + w_, y_ + h_), (300,255,0), 2)
  
    # Label the face as smiling:
    if len(smile_coordinates) > 0:  # As a smile is a list. This works when a smile is detected (>0)
        cv2.putText(frame, 'Smiling!', (x+10, y+h+50), fontScale=2, fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, color=(300, 225, 0), thickness=2)
         # (whole frame, text, location of the text, font size, font type, font color, thickness)
# FONT_HERSHEY_PLAIN
#cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    # Display:
    cv2.imshow('Smile Detector', frame)
    key = cv2.waitKey(1)

    if key==81 or key==113:
        break

# Clean up:
webcam.release()
cv2.destroyAllWindows()

print('Code Completed!')