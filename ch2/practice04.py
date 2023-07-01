import cv2 as cv
import sys

img=cv.imread('soccer.jpg') 

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)	# BGR 컬러 영상을 명암 영상으로 변환

cv.imshow('Color image',img)
cv.imshow('Gray image',gray)

for i in range(1, 11):
    value = i / 10.0
    gray_small=cv.resize(gray,dsize=(0,0),fx=value,fy=value) # 반으로 축소

    cv.imshow('Gray image small, ' + str(value),gray_small)

cv.waitKey()
cv.destroyAllWindows()