########################################################                                            
# Count words in the file example_file.txt             #                     
# @ Carlos Tecles                                      #
########################################################

#import numpy as np
#import cv2
import os

f = open ('example_file.txt', 'r')
lines = f.readlines()
f.close()

count = 0;

for l in lines:
	words = l.split()
	count = count + len(l)

print count
