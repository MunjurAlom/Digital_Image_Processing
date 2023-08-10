import cv2

image = cv2.imread('pink.jpg')

GrayScale = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

cv2.imshow('input',image)
cv2.imshow('output',GrayScale)

cv2.waitKey(0)
cv2.destroyAllWindows()