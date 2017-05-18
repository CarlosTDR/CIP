###############################################
# Produce the following image (the black      #
# frame is 50 pixels wide)                    #
# @ Carlos Tecles                             #
###############################################

import numpy as np
import cv2
import os
from math import sqrt

image = cv2.imread('lena.jpg')

rows, cols = image.shape[:2]
trans_rows = 50 #number of rows to translate
trans_cols = 50 #number of columns to translate

new_rows = rows + 100
new_cols = cols + 100

trans_matrix = np.array([[1,0,trans_cols],[0,1,trans_cols]], 'float32')

image1 = cv2.warpAffine(image, trans_matrix, (new_cols, new_rows))

cv2.imshow('Lena 1', image1)
cv2.waitKey()

cv2.destroyAllWindows()
