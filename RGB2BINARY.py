import cv2

image = cv2.imread('pink.jpg',0)

ret, Binary = cv2.threshold(image,127,256,cv2.THRESH_BINARY)
cv2.imshow('input',image)
cv2.imshow('output',Binary)

cv2.waitKey(0)
cv2.destroyAllWindows()