import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('soccer.jpg')  
# Split the image into its BGR channels
b, g, r = cv.split(img)

# Calculate histograms for each channel
hist_b = cv.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv.calcHist([r], [0], None, [256], [0, 256])

# Plot the histograms
plt.plot(hist_b, color='b', linewidth=1)
plt.plot(hist_g, color='g', linewidth=1)
plt.plot(hist_r, color='r', linewidth=1)

plt.show()