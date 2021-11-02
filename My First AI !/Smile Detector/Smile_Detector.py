# Importing Library
import cv2

# Face and smile classifiers:
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')

print('Code Completed')