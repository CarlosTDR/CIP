###############################################
# Convert Lena image to gray scale and make   #
# a negative.                                 #
# @ Carlos Tecles                             #
###############################################

import numpy as np
import cv2
import os

image = cv2.imread('lena.jpg')

#Converting to gray scale
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Making it negative by changing pixel value per each RGB channel
#to it's contrary value the hard way
for r in range(len(image2)):
    for c in range(len(image2[r])):
        for chan in range(1):
            image2[r][c][chan] = 255 - image2[r][c][chan]



cv2.imshow('lena GnN', image2)

cv2.waitKey()
