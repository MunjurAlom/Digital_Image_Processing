
import cv2
import numpy as np

img1 = cv2.imread('wave.jpg',0)
gamma = 2
img2 = np.power(img1,gamma)
gamma = 3
img3 = np.power(img1,gamma)
gamma = 4
img4 = np.power(img1,gamma)

cv2.imshow('inputImage',img1)
cv2.imshow('Gamma2',img2)
cv2.imshow('Gamma3',img3)
cv2.imshow('Gamma4',img4)

cv2.waitKey(0)
cv2.destroyAllWindows()