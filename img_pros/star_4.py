from colour import Color 
import cv2 as cv2
import numpy as np 
a= input('enter a color=')
b = Color(a)
c = b.hsl
d = tuple(255*x for x in c)
print(d)
print(list(d))
img = cv2.imread('color.png')
hsl1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
green = np.uint8([[list(d)]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print (hsv_green)
f = hsv_green[0][0][0]
if f>10:
    lower = np.array([f-10,50,50], np.uint8)
else:
    lower = np.array([f,100,100, np.uint8])
upper = np.array([f+10,255,255], np.uint8)
colors = cv2.inRange(hsl1, lower,upper)
res = cv2.bitwise_and(img, img, mask = colors)
cv2.imshow('original', img)
cv2.imshow(a, res)
cv2.waitKey(0)
