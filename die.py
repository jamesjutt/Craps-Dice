"""
Program: die.py
Author: James Jutt

This module defines the Die class
"""

from random import randint

class Die(object):
   """This class represents a six-sided die."""

   def __init__(self):
       """Sets the initial face of the die."""
       self.value = 1

   def roll(self):
       """Resets the die's value to a random number from 1 to 6."""
       self.value = randint(1, 6)

   def getValue(self):
       """Returns the current face of the die."""
       return self.value

   def __str__(self):
       """Returns the string representation of the die."""
       return str(self.value)