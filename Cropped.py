import cv2

img = cv2.imread('lena.png')

height,width=img.shape[:2]

start_row,start_col = int(height*.25), int(width*.25)
end_row,end_col = int(height*.75), int(width*.75)

cropped = img[start_row:end_row,start_col:end_col]

cv2.imshow('InputImage',img)
cv2.imshow('CroppedImage',cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()