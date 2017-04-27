###############################################
# Produce these images                        #
# @ Carlos Tecles                             #
###############################################

import numpy as np
import cv2
import os
from math import sqrt

image = cv2.imread('lena.jpg')

image1 = image.astype(np.float)
image1[:,:,:] /= 255
image1 = np.power(image1,2)
image1 *= 255
image1 = image.astype(np.uint8)

image2 = image1.copy()
image2[:,:,0] = 255

image3 = image.copy()
image3 = np.transpose(image3, (1,0,2))
image3[:,:,2] = 255

image4 = image2.copy()
image4 = np.flipud(image4)

cv2.imshow('Lena 1', image1)
cv2.imshow('Lena 2', image2)
cv2.imshow('lena 3', image3)
cv2.imshow('Lena 4', image4)
cv2.waitKey()

cv2.destroyAllWindows()
