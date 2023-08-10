
import cv2
import numpy as np

img1 = cv2.imread('wave.jpg',0)
img2 = np.uint8(np.log1p(img1))

thresh = 1
img3 = cv2.threshold(img2,thresh,255,cv2.THRESH_BINARY)[1]

cv2.imshow('input image',img1)
cv2.imshow('logTransformation',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()