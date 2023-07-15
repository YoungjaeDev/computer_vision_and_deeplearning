import cv2 as cv

nfeatures = 2
while nfeatures <= 512:
    img=cv.imread('mot_color70.jpg') # 영상 읽기
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    sift=cv.SIFT_create(nfeatures=nfeatures)
    kp,des=sift.detectAndCompute(gray,None)

    gray=cv.drawKeypoints(gray,kp,None,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv.imshow(f'sift{nfeatures}', gray)

    nfeatures = nfeatures + nfeatures
    
    # 작으면서 둥근 모양의 키 포인트를 선호하는 것 같음

k=cv.waitKey()
cv.destroyAllWindows()