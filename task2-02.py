########################################################
# Create a list with positive numbers less than 100,   #
# which raised to power 2 are divisible by 6           #
# @ Carlos Tecles                                      #
########################################################

import random
import math
#import pdb
#import numpy as np
#import cv2
import os

#pdb.set_trace()

l = []

def divisible(n):
	n = (n ** 2)
	if n%6 == 0:
		return True
	else:
		return False

while len(l) < 10:
	n = random.randint(0,99)
	if divisible(n) == True:
		l.append(n);

print l
