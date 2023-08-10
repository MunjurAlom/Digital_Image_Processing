import cv2
im = cv2.imread("rose.jpg")
print(type(im))
# <class 'numpy.ndarray'>
print(im.shape)
print(type(im.shape))

h, w, c = im.shape
print('width:  ', w)
print('height: ', h)
print('channel:', c)
