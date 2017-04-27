###############################################
# Produce these images                        #
# @ Carlos Tecles                             #
###############################################

import numpy as np
import cv2
import os
from math import sqrt

image = np.zeros((500,500), 'uint8')
image2 = np.zeros((500,500), 'uint8')
rows, cols = image.shape[:2]

X = cols/2
Y = rows/2

#Distance to center from farest point
distanceCenter = sqrt(pow(X, 2) + pow(Y, 2))

#Distance to center from i,j
def distance (x,y):
    return sqrt(pow(abs(x - X), 2) + pow(abs(y - Y), 2))

#BlackWhite gradient
for i in range(rows):
    for j in range(cols):
        #As far from the center: closer to 0, as close: closer to 1
        image[i,j] = 255 * (distance(i,j)/distanceCenter)


#WhiteBlack gradient
for i in range(rows):
    for j in range(cols):
        #As far from the center: closer to 0, as close: closer to 1
        image2[i,j] = 255 * (distance(i,j)/distanceCenter) * (-1)


cv2.imshow('BlackWhite', image)
cv2.imshow('WhiteBlack', image2)
cv2.waitKey()

cv2.destroyAllWindows()
