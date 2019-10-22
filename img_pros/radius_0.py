import cv2 as cv2
import numpy as np
import math
frame = cv2.imread('color.png')
#read every frame from the camera
    #converting image to hsv
hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    #defining the lower adn higher frame for blue color
lower=np.array([0,100,100])
upper = np.array([20,255,255])
    #defining the threadshold value
mask = cv2.inRange(hsv, lower, upper)
res = cv2.bitwise_and(frame, frame, mask=mask)
_,contour,_ =cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(frame,contour,-1,(0,255,0),1)
cnt = contour[0]
area = cv2.contourArea(cnt)

print("area is")
print(area)
radius = math.sqrt (area/3.14)
print("radius")
print(radius)
cv2.imshow('frame', frame)
cv2.imshow('mask', res)
cv2.waitKey(10000)
