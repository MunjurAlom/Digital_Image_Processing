import cv2

img_1 = cv2.imread("image.jpg")
img_2 = 255-img_1

cv2.imshow("Input Image", img_1)
cv2.imshow("Image Negative", img_2)
cv2.waitKey()