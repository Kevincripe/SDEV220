# Kevin Cripe
# M02 Lab - Case Study: if...else and while
# Write a Python app that will accept student names and 
# GPAs and test if the student qualifies for either the 
# Dean's List or the Honor Roll.


while True:
    # save last name of student as variable
    lname = input("Please enter a last name or press ZZZ to quit ")
    #
    if lname == 'ZZZ':
        break
    # save first name of student as variable
    fname = input("Please enter a first name ")
    # save gpa as a float
    gpa = float(input("Please enter a GPA "))

    # finding if student made list's
    if gpa >= float(3.5):
        print("Student has made the Deans List")
    elif gpa >= float(3.25):
        print("Student has made the Honor Roll")
    else:
        print("This student did not meet requirement")
