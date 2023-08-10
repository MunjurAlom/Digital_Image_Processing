import cv2
import numpy as np

img_1 = cv2.imread("image.jpg", 0)

gamma = 2
img_2 = np.power(img_1, gamma)

gamma = 3
img_3 = np.power(img_1, gamma)

gamma = 4
img_4 = np.power(img_1, gamma)

cv2.imshow("Input Image", img_1)
cv2.imshow("Gamma 2", img_2)
cv2.imshow("Gamma 3", img_3)
cv2.waitKey(10000)