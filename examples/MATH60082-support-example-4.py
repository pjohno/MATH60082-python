#!/usr/bin/env python3
""" 
A program to output some results into a csv file
"""
# libraries and methods
from math import exp,pi

# open a file to output some results
f = open("results.csv",'w')

# let the user know whats happening
print("file opened, outputing results to file")
for i in range(0,101):
    x = i*0.01
    # do some calculations
    y = pi*x*exp(-x)
    # output to string and format if necessary
    str = f" {x} , {y} \n"
    f.write(str)
f.close()
print("file output complete, file closed")


