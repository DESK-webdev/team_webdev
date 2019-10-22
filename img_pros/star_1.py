
import cv2 as cv2
import numpy as np
print('enter path:')
x=input()
frame = cv2.imread(x)

#read every frame from the camera
    #converting image to hsv
hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    #defining the lower adn higher frame for blue color
lower=np.array([0,50,50])
upper = np.array([20,255,255])
    #defining the threadshold value
mask = cv2.inRange(hsv, lower, upper)
res = cv2.bitwise_and(frame, frame, mask=mask)
cv2.imshow('frame', frame)
cv2.imshow('mask', res)
cv2.waitKey(10000)
