import cv2 as cv2
import numpy as np
import math
frame = cv2.imread('2.jpeg')
#read every frame from the camera
    #converting image to hsv
hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    #defining the lower adn higher frame for blue color
lower=np.array([0,100,100])
upper = np.array([20,255,255])
    #defining the threadshold value
mask = cv2.inRange(hsv, lower, upper)
res = cv2.bitwise_and(frame, frame, mask=mask)
_,contour, _ =cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(frame,contour,-1,(0,255,0),1)
cnt = contour[0]
area = cv2.contourArea(cnt)
print(area)
radius = math.sqrt (area/3.14)
print(radius)
frame = cv2.resize(frame, None, fx=2, fy=2,interpolation=cv2.INTER_CUBIC)
frame =cv2.putText(frame,"the radius is: "+str(radius), (0,150),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),1,cv2.LINE_AA)
cv2.imshow('frame', frame)

cv2.imshow('mask', res)
cv2.waitKey(10000)

