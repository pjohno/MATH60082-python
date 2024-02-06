#!/usr/bin/env python3
""" 
A program to create a pdf figure of the sin function
"""
import matplotlib.pyplot as plt
import numpy 
from math import pi

x = numpy.arange(0, 3*pi, 0.02*pi)  # creates an array of data x[i] = 0 + i*0.02*pi such that x_i \leq 3*pi
y = numpy.sin(x)       

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y = sin(x)")
plt.savefig('example-figure.pdf', dpi=300, format='pdf', bbox_inches='tight')