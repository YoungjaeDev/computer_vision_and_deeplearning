import cv2 as cv
import sys

def draw(event,x,y,flags,param):
    global ix,iy
    
    if event==cv.EVENT_LBUTTONDOWN:	# 마우스 왼쪽 버튼 클릭했을 때 초기 위치 저장
        ix,iy=x,y
    elif event==cv.EVENT_LBUTTONUP:	# 마우스 왼쪽 버튼 클릭했을 때 직사각형 그리기
        cv.rectangle(img,(ix,iy),(x,y),(0,0,255),2)
    
        patch=img[iy:y,ix:x,:]
        
        patch1=cv.resize(patch,dsize=(0,0),fx=5,fy=5,interpolation=cv.INTER_NEAREST)
        patch2=cv.resize(patch,dsize=(0,0),fx=5,fy=5,interpolation=cv.INTER_LINEAR)
        patch3=cv.resize(patch,dsize=(0,0),fx=5,fy=5,interpolation=cv.INTER_CUBIC)

        cv.imshow('Original',img)
        cv.imshow('Resize nearest',patch1) 
        cv.imshow('Resize bilinear',patch2) 
        cv.imshow('Resize bicubic',patch3) 
    
    cv.imshow('Drawing',img)

img=cv.imread('rose.png')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
cv.namedWindow('Drawing')
cv.imshow('Drawing',img)

cv.setMouseCallback('Drawing',draw)

while(True):
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()      
        break