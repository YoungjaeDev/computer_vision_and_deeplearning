import cv2 as cv
import sys
import os

img = cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다')

img2 = cv.imread('dog.jpeg')

if img2 is None:
    sys.exit('파일을 찾을 수 없습니다')
    
cv.imshow('Image 1 Display', img)
cv.imshow('Image 2 Display', img2)

cv.waitKey()
cv.destroyAllWindows()