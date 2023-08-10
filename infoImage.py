import cv2

img = cv2.imread('luffy.jpg')

cv2.imshow('input',img)
print(img.shape)
print('Height: ',img.shape[0])
print('Width: ',img.shape[1])
print('Channels: ',img.shape[2])

cv2.waitKey(0)
cv2.destroyAllWindows()