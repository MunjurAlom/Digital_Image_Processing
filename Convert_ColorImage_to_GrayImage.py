#import opencv
import cv2

#load imagess
img = cv2.imread('image.jpg')
#show image
cv2.imshow('Original',img)
cv2.waitKey()

#convert grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#save to new file
cv2.imwrite('newImage.png', gray_img)
cv2.imshow("new image grayscale", gray_img)
cv2.waitKey(0)
#destory window
cv2.destroyAllWindows()
