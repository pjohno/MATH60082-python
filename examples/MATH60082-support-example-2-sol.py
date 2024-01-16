#!/usr/bin/env python3
""" 
A program to calculate the area of a circle, with user input for the radius
"""
# libraries and methods
import math

# declare variables and assign values
radius = float(input())

# do the calculations
area = math.pi * radius * radius

# output the results
print("The area of a circle with radius ",radius," is ",area)
