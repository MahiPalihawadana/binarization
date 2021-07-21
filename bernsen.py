# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 12:16:27 2021

@author: Dilki palihawadana
"""

# importing required libraries
import mahotas
import mahotas.demos
import numpy as np
from pylab import imshow, gray, show
from os import path
from skimage import io

# loading the image
#photo = mahotas.demos.load('luispedro')


# loading image as grey
#photo = mahotas.demos.load('luispedro', as_grey = True)

photo = io.imread("img2.jpg", as_gray=True)

# converting image type to unit8
# beacuse as_grey returns floating values
photo = photo.astype(np.uint8)

# showing original image
print("Image")
imshow(photo)
show()

# bernsen threshold
photo = mahotas.thresholding.bernsen(photo, 7, 200)


print("Image with bernsen threshold")

# showing image
imshow(photo)
show()
