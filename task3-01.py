###############################################
# Set the blue channel of Lena to minimum     #
# value and display the image.                #
# @ Carlos Tecles                             #
###############################################

import numpy as np
import cv2
import os

image = cv2.imread('lena.jpg')
image[:,:,0] = 0;
cv2.imshow('lena',image)

cv2.waitKey()
