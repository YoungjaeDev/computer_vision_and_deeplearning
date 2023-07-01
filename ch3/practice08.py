import cv2 as cv
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import time

def myEqualizeHist(gray_img):
    h,w = gray_img.shape[:2]

    img_flattened = gray_img.flatten()

    img_counter = Counter(img_flattened)

    zero_list = [0] * 256

    for key, value in img_counter.items():
        zero_list[key] = value / (h*w)
        
    zero_list_cumulative = np.cumsum(zero_list)
    
    zero_list_cumulative = np.round(zero_list_cumulative * 255)

    # Apply the transformation to img
    img_transformed = zero_list_cumulative[gray_img]
    
    return img_transformed

img=cv.imread('mistyroad.jpg') 

gray_img=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

start=time.time()
img_transformed = myEqualizeHist(gray_img)
print("myEqualizeHist time:", time.time()-start)

start=time.time()
equal=cv.equalizeHist(gray_img)
print("OpenCV EqualizeHist time:", time.time()-start)

# Display the original and transformed images
plt.subplot(1, 3, 1)
plt.imshow(gray_img, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(img_transformed, cmap='gray')
plt.title('Transformed Image')

plt.subplot(1, 3, 3)
plt.imshow(equal, cmap='gray')
plt.title('OpenCV equalize Image')

plt.show()

"""
myEqualizeHist time: 0.07615470886230469
OpenCV EqualizeHist time: 0.000591754913330078
"""