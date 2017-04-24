########################################################                                            #
# Print how many times each word from file             #
# example_file.txt occurs.                             #
# @ Carlos Tecles                                      #
########################################################

#import numpy as np
#import cv2
import os

f = open ('example_file.txt', 'r')
text = f.read()
f.close()

distinctWords = []
count = []

#I know is a pretty messy way
for w in text.split():
	if w not in distinctWords:
		distinctWords.append(w)
		count.append(1)
	else:
		count[distinctWords.index(w)] = count[distinctWords.index(w)] + 1

for w in distinctWords:
	print w + " " + str(count[distinctWords.index(w)])
