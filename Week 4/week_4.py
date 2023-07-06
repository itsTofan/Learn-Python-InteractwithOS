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