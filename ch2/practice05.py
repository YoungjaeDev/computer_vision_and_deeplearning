import cv2 as cv
import sys

cap=cv.VideoCapture(0,cv.CAP_DSHOW)	# 카메라와 연결 시도

if not cap.isOpened():
    sys.exit('카메라 연결 실패')
    
while True:
    ret,frame=cap.read()			# 비디오를 구성하는 프레임 획득
    
    global gray
    
    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break
        
    key=cv.waitKey(1)	# 1밀리초 동안 키보드 입력 기다림
    if key==ord('q'):	# 'q' 키가 들어오면 루프를 빠져나감
        break 
    elif key==ord('g'):
        gray=1
    elif key==ord('c'):
        gray=0
    
    if gray:
        frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)	# BGR 컬러 영상을 명암 영상으로 변환

    cv.imshow('Video display',frame)
    
cap.release()			# 카메라와 연결을 끊음
cv.destroyAllWindows()