# Importing Image class from PIL module
from PIL import Image

# Opens a image in RGB mode
im = Image.open("image.jpg")

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size

# Setting the points for cropped image
left = 20
top = height / 10
right = 150
bottom = 4 * height / 7

# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))

# Shows the image in image viewer
im1.show()
