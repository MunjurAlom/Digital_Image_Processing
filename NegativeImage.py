import cv2

img = cv2.imread('wave.jpg',0)
img2 = 255 - img

cv2.imshow('inputImage',img)
cv2.imshow('negativeImage',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
