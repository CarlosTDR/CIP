###############################################
# Produce these images                        #
# @ Carlos Tecles                             #
###############################################

import numpy as np
import cv2
import os
from math import sqrt

image = np.zeros((500,1000), 'uint8')

image2 = image.copy()
image2[:,:] = 1
image2 *= 255

rows, cols = image2.shape[:2]

X = cols/2
Y = rows/2

#Horizant WhiteBlack gradient
for j in range(cols):
    #As far from the center: closer to 0, as close: closer to 1
    image2[:,j] = abs(float(j) - X)/(cols) * 255 * -1

cv2.imshow('BlackWhite', image2)
cv2.waitKey()

cv2.destroyAllWindows()
