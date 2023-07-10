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


#black box vs white box
#White-box testing (clear-box/transparent testing) relies on the test creator's knowledge of the software
#being tested to construct the test cases

#black box testing - software being tested is treated like an opaque box, tester doesn't know the internal
#of the software works
#black box test written with awareness of what the program is supposed to do, its requirements or specification
#but not how it does it


#other type of test
#intergration test verify that interactions between the different pieces of code in integrated enviroments are
#working the way we expect them to.
#the goal to verify these kind of interactions and make sure the system works

#regression test - written as part of debugging and troubleshooting process to verify an issue or error has
#been fixed once it's been identified

#smoke test / build verification test
#load test to verify the system behaves well when it's under significant load


#Test-Driven Development TDD creating the test before writing the code


#Error and Execption
#the code in the except block is only executed if one of the instructions in the try block
#raises an error of the matching type
def character_frequency(filename):
    """counts the frequency of each character in the given file"""
    # First try to open the file
    try:
        f = open(filename)
    except OSError:
        return None
    
    #now process the file
    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close
    return characters

#raising errors
def validate_user(username, minlen):
    assert type(username) ==  str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

#Testing for expected error
