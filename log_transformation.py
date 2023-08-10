import cv2
import numpy as np

img_1 = cv2.imread("image.jpg")
img_2 = np.uint8(np.log1p(img_1))
thresh = 1
img_3 = cv2.threshold(img_2, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("Input Image", img_1)
cv2.imshow("Log Transformed", img_3)
cv2.waitKey(10000)