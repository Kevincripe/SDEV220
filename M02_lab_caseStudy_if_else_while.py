# Kevin Cripe
# M02 Lab - Case Study: if...else and while
# Write a Python app that will accept student names and 
# GPAs and test if the student qualifies for either the 
# Dean's List or the Honor Roll.

import sys
# save last name as variable
lname = input("Please enter a last name or press ZZZ to quit ")
# if block to detect quit response
if lname == 'ZZZ' or 'zzz':
    sys.exit()
# save first name as variable
fname = input("Please enter a first name ")

