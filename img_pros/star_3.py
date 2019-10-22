import  cv2 as cv2
import numpy as np 
path=input()
img = cv2.imread(path)
hsl=cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
lower = np.uint8([0,0,100])
upper = np.uint8([255,255,255])
white = cv2.inRange(hsl, lower, upper)
res = cv2.bitwise_and(img,img, mask=white)
cv2.imshow('img',img)
cv2.imshow('white',res)
cv2.waitKey(10000)
