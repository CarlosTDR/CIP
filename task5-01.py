###############################################
# How to create a negatve of an image with a  #
# proper color map                            #
# @ Carlos Tecles                             #
###############################################

import numpy as np
import cv2
import os
from math import sqrt

image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

color_min = np.array([255,255,255], 'uint8')
color_max = np.array([0,0,0], 'uint8')

color_map = np.zeros((256,3), 'uint8')

#fill color map
for i in range(256):
    color_map[i,:] = (1.0 - i/255.0) * color_min + i/255.0 * color_max

print 'color_map='
print color_map

image2 = color_map[image,:]

print 'image.shape=' + str(image.shape)
print 'image2.shape=' + str(image2.shape)

cv2.imshow('Lena', image)
cv2.imshow('Lena with negative color map', image2)

cv2.waitKey()

cv2.destroyAllWindows()
