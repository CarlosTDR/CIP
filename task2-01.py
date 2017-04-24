###############################################
# Ask user for a number. If it is even,       #
# multiply it by 3,                           #
# otherwise if it is greater than 10 add 3,   #
# otherwise                                   #
# add 1                                       #
# @ Carlos Tecles                             #
###############################################

#import numpy as np
#import cv2
import os

number = int(raw_input('\n Introduce number: '))
print(" " + str(number))

if number%2 == 0:
	number = number * 3
elif number > 10:
	number = number + 2
else:
	number = number + 1

print(" " + str(number))
