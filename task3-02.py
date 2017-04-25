###############################################
# Set the H, S and V channels in HSV color    #
# space of Lena image to maximum / minimum    #
# value and display the result.Experiment     #
# with other value.                           #
# @ Carlos Tecles                             #
###############################################

import numpy as np
import cv2
import random
import copy
import os

image = cv2.imread('lena.jpg')

#Converting to HSV color space
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#Creating copy in memory of different images
imageH = copy.deepcopy(image2)
imageS = copy.deepcopy(image2)
imageV = copy.deepcopy(image2)

list = [0,255]

#Giving random HSV values
imageH[:,:,0] = random.choice(list)
imageS[:,:,1] = random.choice(list)
imageV[:,:,2] = random.choice(list)

print "\n Random maximum or minimum HSV values"

#Converting back to RGB
imageH = cv2.cvtColor(imageH, cv2.COLOR_HSV2BGR)
imageS = cv2.cvtColor(imageS, cv2.COLOR_HSV2BGR)
imageV = cv2.cvtColor(imageV, cv2.COLOR_HSV2BGR)

cv2.imshow('lena Hr', imageH)
cv2.imshow('lena Sr', imageS)
cv2.imshow('lena Vr', imageV)


cv2.waitKey()
cv2.destroyAllWindows()
