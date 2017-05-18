###############################################
# Create the following color maps and images  #
# @ Carlos Tecles                             #
###############################################

import numpy as np
import cv2
import os
from math import sqrt

def define_color_map(color_I, color_II, color_III, color_IV):
    color_map = np.zeros((256,3), 'uint8')
    #filling color map with colors
    for i in range(256):
        #Colors are gradient color-white tho, read next comment
        color_map[i,:] = (1.0 - i/255.0) * color_I + (0.33 - i/255.0) * color_II + (0.66 - i/255.0) * color_III + i/255.0 * color_IV
    return color_map

#Define 3 colors map
def define_color_map_3(color_I, color_II, color_III):
    color_map = np.zeros((256,3), 'uint8')
    #fill color map with colors
    for i in range(128):
        color_map[i,:] = (1.0 - i/127.0) * color_I + i/127.0 * color_II
    for i in range(128,256):
        color_map[i,:] = (1.0 - (i - 128.0)/127.0) * color_II + (i - 128.0)/127.0 * color_III
    return color_map

#Apply color map
def create_color_map_image(color_map, width, height):
    map_image = np.zeros((height, width), 'uint8')
    for i in range(width):
        map_image[:,i] = float(i)/(width-1) * 255
    return color_map[map_image,:]

color_1 = np.array([127,127,127], 'uint8')
color_2 = np.array([0,255,255], 'uint8')
color_3 = np.array([0,0,255], 'uint8')

color_map = define_color_map_3(color_1, color_2, color_3)

#Att: it doesn't work if you use rose instead of rose.png
image = cv2.imread('rose.png', cv2.IMREAD_GRAYSCALE)

image2 = create_color_map_image(color_map, 900, 400)

image3 = color_map[image,:]

print 'color_map='
print color_map

#print 'image.shape=' + str(image.shape)
#print 'image2.shape=' + str(image2.shape)

cv2.imshow('rose', image)
cv2.imshow('Color map', image2)
cv2.imshow('Rose with color map', image3)

cv2.waitKey()

cv2.destroyAllWindows()
