# 1. Import OpenCV.
import cv2

# 2. Import our pre-trained car classifier << Downloaded from GitHub >>. (I had to ad the whole path for it to work)
trained_car_file = 'D:\Escritorio\Programming\My First AI !\Car & Pedestrian Tracker.py\haarcascade_car_detector.xml'

# 2.1. Create or car classifier:
car_tracker = cv2.CascadeClassifier(trained_car_file )

# 3. Import a image of a car.
img_file = 'D:\Escritorio\Programming\My First AI !\Car & Pedestrian Tracker.py\C1.jpg'

# 3.1. Create a OpenCV image (So it can work with it) << It reads all the pixels data of the image file as a multidimentional array >>:
img = cv2.imread(img_file)

# 4. Convert the image to grayscale (needed for haar cascade)
grayscaled_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 5. Detect cars (Aplly the classifier to the grayscaled image, no matter the size of the car)
cars = car_tracker.detectMultiScale(grayscaled_image)

print(cars)
# This prints the location of the car with square/rectangle coordinates.

# 6.  Draw rectangles around the cars:
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 3)
    

# 7. Display the image:
cv2.imshow('Image Car Detector', img)

# Don't autoclose (Wait for a key press)
cv2.waitKey()


print('Code Completed')
