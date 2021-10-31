## How To Read A Video ##

import cv2 

# TODO: Hacer
# FIXME: Hacer

capture = cv2.VideoCapture('D:\Escritorio\Programming\My First AI !\Car & Pedestrian Tracker.py\Car_Video.mp4')

while (capture.isOpened()):
    ret, frame = capture.read()
    if (ret == True):
      cv2.imshow('webCam', frame)
      if (cv2. waitKey(1) == ord ('s')):
          break
    else:
      break

capture.release()
cv2.destroyAllWindows