#!/usr/bin/env python3
""" 
A program to prompt user for current date, and then calculate how many years it is since Manchester United last won the league
"""
# libraries and methods
from datetime import timedelta,date

# declare variables and assign values
dateLastWon = date(2012,8,19)               # date on last day of 2012/2013 season was 19th May 2013
day = input("Input day of month (1-31)")    # input day of month
month = input("Input month (1-12)")         # input month
year = input("Input year ")                 # input year
dateCurrent = date(year,month,day)          # create current date

# calculate the number of years
yearsSinceWon = (dateCurrent-dateLastWon).days

# output the results
print("On ",dateLastWon,", it will be ",yearsSinceWon," years since Manchester united last won the Premier League.")