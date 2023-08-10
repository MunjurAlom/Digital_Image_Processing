import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img1.png')

cv2.imshow('input',img)


plt.hist(img.ravel(), 256 ,[0,256])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()