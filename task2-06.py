########################################################                                            
# Print distinct words from file example_file.txt      #                     
# @ Carlos Tecles                                      #
########################################################

#import numpy as np
#import cv2
import os

f = open ('example_file.txt', 'r')
text = f.read()
f.close()

DistinctWords = []

for w in text.split():
	if w not in DistinctWords:
		DistinctWords.append(w)

print DistinctWords
print len(DistinctWords)
