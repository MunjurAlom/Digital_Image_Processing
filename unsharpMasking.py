# Importing Image and ImageFilter module from PIL package
from PIL import Image, ImageFilter


# creating a image object
im1 = Image.open('swobg (1).jpg')

# applying the unsharpmask method
im1.show()
im2 = im1.filter(ImageFilter.UnsharpMask(radius=3, percent=200, threshold=5))
im3 = im2.save('C:/Users/Munjur Alom/Desktop/s/swobg (1).jpg')

im2.show()
