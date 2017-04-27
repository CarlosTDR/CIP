###############################################
# Produce these images                        #
# @ Carlos Tecles                             #
###############################################

import numpy as np
import cv2
import os
from math import sqrt

image = np.zeros((500,500,3), 'uint8')

image[:,:,2] = 255 #Set to Red

rows, cols = image.shape[:2]

X = cols/2
Y = rows/2

#Horizant RedGreen gradient
for j in range(cols):
    #As closer to the right it gets less Red and more Green
    image[:,j,1] = float(j)/(cols - 1) * 255
    image[:,j,2] = float(j)/(cols - 1) * 255 * -1

cv2.imshow('GreenRed', image)
cv2.waitKey()

cv2.destroyAllWindows()
