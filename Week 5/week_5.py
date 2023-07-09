#Testing in Python
#Software Testing is the process of evaluating computer code to determine whether or not it does what you expect it to do
"""
* Manual Testing is executing a script with different value and returned expected value.
* Automated Testing, we write the code to do the test using test case
    - Unit Test used to verify that small, isolated parts of a program are correct
    characteristic is isolation and using test enviroments
    
""" 

#Unit Test
import re

def rearrenge_name(name):
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])


#Edge Cases inputs to our code that produce unexpected results and are found at the extreme ends
#of the ranges of input we imagine our programs will typically work with
