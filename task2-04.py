########################################################
# Sort list of Person objects according                #
# to age/name/surname                                  #
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
			print self.nazwa + " " + self.nawisko + " is " +str(self.wiek) +  " and " + self.plec

list = [Person("Gandalf", "The grey", 11000 , "Ainur"),
	 	Person("Galadriel","White lady", 10000 , "Elve"),
		Person("Aragorn", "Strider", 203 , "Human-Elve")]

print "\n List created: \n"
for x in list:
	x.toString();

print "\n Sorting by age for example from lower to upper ..."
list2 = sorted(list, key = lambda Person: Person.wiek)

print " Checking sorting ... \n"
for x in list2:
	x.toString()
