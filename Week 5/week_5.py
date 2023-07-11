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


#practice lab
my_list = [27, 5, 9, 6, 8]

def RemoveValue(myVal):
    if myVal not in my_list:
        raise ValueError("Value must be in the given list")
    else:
        my_list.remove(myVal)
    return my_list

print(RemoveValue(27))

my_word_list = ['east', 'after', 'up', 'over', 'inside']

def OrganizeList(myList):
    for item in myList:
        assert type(myList) ==  str, " list must be a list of strings"
    myList.sort()
    return myList

print(OrganizeList(my_new_list))

my_new_list = [6, 3, 8, "12", 42]
print(OrganizeList(my_new_list))

import random

participants = ['Jack','Jill','Larry','Tom']

def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    if my_participant_dict['Larry'] == 9:
        return True
    else:
        return False
    
print(Guess(participants))

# Revised Guess() function
def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    if my_participant_dict['Larry'] == 9:
        return True
    else:
        return False

participants = ['Cathy','Fred','Jack','Tom']
print(Guess(participants))


""""
Test
cd ~/data
ls
cat user_emails.csv
cd ~/scripts
ls
cat emails.py
python3 emails.py Blossom Gill
nano ~/scripts/emails_test.py
#!/usr/bin/env python3
import unittest

from emails import find_email
class EmailsTest(unittest.TestCase):
  def test_basic(self):
    testcase = [None, "Bree", "Campbell"]
    expected = "breee@abc.edu"
    self.assertEqual(find_email(testcase), expected)
if __name__ == '__main__':
  unittest.main()

chmod +x emails_test.py
./emails_test.py

python3 emails.py Kirk

nano emails_test.py
  def test_one_name(self):
    testcase = [None, "John"]
    expected = "Missing parameters"
    self.assertEqual(find_email(testcase), expected)

./emails_test.py
nano emails.py
#!/usr/bin/env python3
import sys
import csv
def populate_dictionary(filename):
  Populate a dictionary with name/email pairs for easy lookup.
  email_dict = {}
  with open(filename) as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
      name = str(row[0].lower())
      email_dict[name] = row[1]
  return email_dict
def find_email(argv):
  Return an email address based on the username given.
  # Create the username based on the command line input.
  try:
    fullname = str(argv[1] + " " + argv[2])
    # Preprocess the data
    email_dict = populate_dictionary('/home/{{ username }}/data/user_emails.csv')
    # Find and print the email
    return email_dict.get(fullname.lower())
  except IndexError:
    return "Missing parameters"
def main():
  print(find_email(sys.argv))
if __name__ == "__main__":
  main()

./emails_test.py

"""