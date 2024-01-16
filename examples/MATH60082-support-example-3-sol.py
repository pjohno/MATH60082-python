#!/usr/bin/env python3
""" 
A program to prompt user for current date, and then calculate how many years it is since Manchester United last won the league
"""
# libraries and methods
from datetime import timedelta,date

# declare variables and assign values
dateLastWon = date(2013,4,22)               # actually won the league on 22nd April 2013
day = int(input("Input day of month (1-31)"))    # input day of month, must be integers, and should really error check values
month = int(input("Input month (1-12)"))         # input month, must be integers, and should really error check values
year = int(input("Input year "))                 # input year, must be integers, and should really error check values
dateCurrent = date(year,month,day)          # create current date

# calculate the number of years
yearsSinceWon = (dateCurrent-dateLastWon).days # this is number of days, divide by 
yearsSinceWon = yearsSinceWon / 365.

# output the results
print("On {}, it will be {:.2f} years since Manchester united last won the Premier League.".format(dateCurrent,yearsSinceWon))