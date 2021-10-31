# 1. Import OpenCV.
import cv2

# 2. Import our pre-trained car classifier << Downloaded from GitHub >>. (I had to ad the whole path for it to work)
trained_car_file = 'D:\Escritorio\Programming\My First AI !\Car & Pedestrian Tracker.py\haarcascade_car_detector.xml'
car_tracker = cv2.CascadeClassifier(trained_car_file )

# 3. Import a video of cars.
video = cv2.VideoCapture('D:\Escritorio\Programming\My First AI !\Car & Pedestrian Tracker.py\Car_Video.mp4')

if (video.isOpened() == False):
	print("Error opening the video file")

# Run forever until car stops or something.
while True:

    # 3.1. Read the current frame:
    read_succesful, frame = video.read()

    if read_succesful:    # Safe coding.
    # 4. Must convert to grayscale.
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # 5. Detect cars (Aplly the classifier to the grayscaled image, no matter the size of the car)
    cars = car_tracker.detectMultiScale(grayscaled_frame)

    # This prints the location of the car with square/rectangle coordinates.
    print(cars)
    
    # 6.  Draw rectangles around the cars:
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)
        

    # . Display the video:
    cv2.imshow('Video Car Detector', frame)

    # Don't autoclose (Wait for a key press)
    cv2.waitKey(1)

print('Code Completed')

