###############################################
# Make a color negative (make a negative of   #
# each channel of Lena image separately and   #
# display the result).                        #
# How can it be done faster?                  #             #
# @ Carlos Tecles                             #
###############################################

import numpy as np
import cv2
import copy
import os

image = cv2.imread('lena.jpg')

#Creating copy in memory of different images
image2 = copy.deepcopy(image)

image[:,:,0] = 255 - image[:,:,0]
image[:,:,1] = 255 - image[:,:,1]
image[:,:,2] = 255 - image[:,:,2]

cv2.imshow('lena', image)

image2[:,:,:] = 255 - image2[:,:,:]

cv2.imshow('lena', image)

cv2.waitKey()
