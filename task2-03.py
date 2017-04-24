########################################################
# Write a class Person to store information            #
# about the name, surname and age of a person.         #
# Create a list of such objects.                       #
# Copy the list to other list (make a deep             #
# copy: copy not only list but also the objects)       #
# @ Carlos Tecles                                      #
########################################################

import copy
#import numpy as np
#import cv2
import os

class Person:
	def __init__(self, name, surname, age, race):
		self.nazwa = name
		self.nawisko = surname
		self.wiek = age
		self.plec = race

	def toString (self):
			print self.nazwa + " " + self.nawisko + " is " + self.wiek +  " and " + self.plec

list = [Person("Gandalf", "The grey", "11.000", "Ainur"),
	 	Person("Galadriel","White lady","10.000", "Elve"),
		Person("Aragorn", "Strider", "203", "Human-Elve")]

print "\n List created: \n"
for x in list:
	x.toString();

print "\n Making copy ..."
list2 = copy.deepcopy(list)

print " Checking copy ... \n"
for x in list2:
	x.toString()
