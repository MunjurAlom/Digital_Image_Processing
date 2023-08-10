import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('download.jpg',cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((2,2), np.uint8)

dialation = cv2.dilate(mask, kernel, iterations=1)
erosion = cv2.erode(mask, kernel, iterations=1 )
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

titles = ['Image','Mask','Dialation','Erosion','Opening','Closing']
images = [img,mask,dialation,erosion,opening,closing]

for i in range (6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title([titles[i]])
    plt.xticks([]),plt.yticks([])

plt.show()