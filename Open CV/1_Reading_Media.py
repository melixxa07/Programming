import cv2
print('Package Imported')

#&                                                     -- Read Images, Videos and Webcam --

#&  FOR IMAGES: 
'''
# To import the image:
img = cv2.imread('D:\Escritorio\Programming\Open CV\Media\Structure.png')
# To display the image:
cv2.imshow('Output', img)     # cv2.imshow(Name of the window, The image we want to display) => Arguments
# As it apears immediately we have to add a delay
cv2.waitKey(0)   # 0 => Infinite delay;    1000 => 1 second
'''


#&  FOR VIDEOS: 
'''
# To import a video:
cap = cv2.VideoCapture('D:\Escritorio\Programming\Open CV\Media\Switzerland_Driving.mp4')
# To display the video:
# As a video is a sequence of images, we have to make a while loop to see it one by one.
while True:
    read_successful, img = cap.read()   # This will save the image in varible 'img' and will tell us if it was done succesfully or not
    cv2.imshow('Video', img)
    # To break out of the loop we add a 'Q' press:
    ##if cv2.waitKey(1)==81 or cv2.waitKey(1)==113:
        ##break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''


#&  FOR WEBCAM: 
'''
# To grab webcam feed:
webcam = cv2.VideoCapture(0)   # If we have another camera conected to the PC, you can read it putting number 1
#webcam.set(3, 640)     # Width (id for width, number of width)
#webcam.set(4, 480)     # Height (id for height , number of width)
#webcam.set(10, 100)    # Brigtness   (id for brigtness, brightness)
# To read and display the camera/video:
while True:
    read_successful, img = webcam.read()
    cv2.imshow('Camera', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''