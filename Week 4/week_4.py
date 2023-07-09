#Managing Data and Process
#input function
import os

name = input ("Enter your name: ")
print("Hi " + name)

#Times Converter
def to_seconds (hours, minutes, seconds):
    return hours*3600+minutes*60+seconds

print("Welcome to this time converter")

cont = "y"
while(cont.lower() == "y"):
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
    print()
    cont = input("Do you want to do another conversion? [y to continue] ")

print("Good Bye " + name + "!")

#Standard streams
#I/O Streams is the basic mechanish for performing input and output operations in your programs.
#STDIN standard input ie from keyboard
#STDOUT standard ouput ie to display
#STDERR standard error ie to display
data = input("This will come from STDIN: ")
print ("Now we write it to STDOUT: " + data)
#print("Now we generate an error to STDERR: " + data + 1)

#Enviroment Variables
#Shell is command line interface used to interact with operating system ie bash on linus, zsh, fish
#Python program get executed inside a shell command line evrironment
#The variables set in that env are another source of information that we can use in our scripts
#PATH variable
print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))

#Command line Argument and exit status is a parameters that are passed to a program when it's started
import sys
print(sys.argv)

#exit status or exit code - value returnn by a program to the shell
#0 is success else is error


#------------------------------
#Python sub processing - running system commands
import subprocess
#subprocess.run(["date"], shell=True)
#subprocess.run(["sleep", "2"], shell=True)
result = subprocess.run(["ls","this_file_does_not_exist"], shell=True)
print(result.returncode)

#obtain the output of system command
result = subprocess.run(["host","8.8.8.8"], capture_output=True, shell=True)
print(result.returncode)
print(result.stdout.decode().split)

#advance subprocess management - 
my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp"], my_env["PATH"])
result = subprocess.run(["myapp"], env=my_env, shell=True)

#Processing log file
#log file using regular expression
#read file line by line if the file is big

import sys
import re

logfile = "syslog.txt"
usernames = {}
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] =  usernames.get(name, 0) + 1

print(usernames)
print (usernames)

#Final Lab
"""
cat ~/data/fishy.log
cd ~/scripts
nano find_error.py

#!/usr/bin/env python3
import sys
import os
import re
def error_search(log_file):
  error = input("What is the error? ")
  returned_errors = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      error_patterns = ["error"]
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
        returned_errors.append(log)
    file.close()
  return returned_errors
  
def file_output(returned_errors):
  with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
    for error in returned_errors:
      file.write(error)
    file.close()
if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)

sudo chmod +x find_error.py
./find_error.py ~/data/fishy.log
CRON ERROR Failed to start
cat ~/data/errors_found.log
"""