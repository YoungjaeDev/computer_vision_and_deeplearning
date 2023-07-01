import cv2 as cv
import sys

img=cv.imread('girl_laughing.jpg') 
  
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.rectangle(img,(830,30),(1000,200),(0,0,255),2)	# 직사각형 그리기
cv.putText(img,'laugh',(500,500),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)	# 글씨 쓰기

cv.arrowedLine(img, pt1=(830,30), pt2=(500,500), color=(0,255,0), thickness=1, line_type=cv.LINE_8, shift=0, tipLength=0.1)

cv.imshow('Draw',img)

cv.waitKey()
cv.destroyAllWindows()