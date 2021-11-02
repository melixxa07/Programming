# Importing Library:
import cv2

# Face and smile classifiers:
face_detector = cv2.CascadeClassifier('D:\Escritorio\Programming\My First AI !\Face Detector\haarcascade_frontalface_default.xml')
####smile_detector = cv2.CascadeClassifier('D:\Escritorio\Programming\My First AI !\Smile Detector\haarcascade_smile.xml')

# Grab Webcam feed:
webcam = cv2.VideoCapture(0)

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

    # Run smile stection within each of those faces:
    for (x, y, w, h) in face_coordinates:

        # Draw a rectangle around faces:
         cv2.rectangle(frame, (x, y), (x+w, y+h), (300,255,0), 3)
    print(face_coordinates)
    ###smile_coordinates = smile_detector.detectMultiScale(grayscaled_frame)

    # Display:
    cv2.imshow('Smile Detector!', frame)
    key = cv2.waitKey(1)

    if key==81 or key==113:
        break

# Clean up:
webcam.release()
cv2.destroyAllWindows()

print('Code Completed!')