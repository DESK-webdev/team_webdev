import cv2 as cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(True):
    #read every frame from the camera
    _,frame = cap.read()
    #converting image to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    #defining the lower adn higher frame for blue color
    lower=np.array([110,50,50])
    upper = np.array([130,255,255])
    #defining the threadshold value
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', res)
    if cv2.waitKey(10) & 0xFF == 27: #Press q esc to escape
                cap.release()
                cv2.destroyAllWindows()
                break  
