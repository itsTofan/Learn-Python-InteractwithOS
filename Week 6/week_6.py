#Bash Scripting

"""
-- Basic Linux Commands
echo print message to screen
cat to content of file
ls list of file
chmod to change permission of file
mkdir to create new directoru
cd newdirectory
pwd to print current directory
cp to copy file cp ../spider.txt .
touch myfile.txt to create empty file
ls -l to see content of directory, -l to see details
ls -la to see content including hidden file
mv myfile.txt emptyfile.txt rename or move file
cp spider.txt yetanotherfile.txt
rm * to delete all file
cd .. to go back 1 directory
rmdir to delete empty directory only
"""

"""
I/O Stream in BASH
Redirection - is the process of sendong a stream to a different destionation
./stdout_example.py > new_file.txt print to a file
./stdout_example.py >> new_file.txt append to a file 
"""

"""
-- Pipe and Pipelines
Pipes connect the output of one program to the input of another in order to pass data between programs
ls -l | less display content of folder
cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head

--Singaling Process
- Signals are token delivered to running processes to indicate a desired action
Ping command sending ICMP packet to website
CTRL-C - Finish - SIGINT
CTRL-Z - STOP - SIGSTOP
KILL - SIGTERM

--BASH Script
ps list all current run process
free memory
uptime how long computer has been on

line="-----------------------------"
echo "Starting at: $(date)" ; echo $line

echo "UPTIME" ; uptime ; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: ($date)"

--Using variable and Globs
example=hello - make sure no space
echo $example
globs - character that allow us create list of file
echo *.py
echo c*
echo *
echo ?????.py
glob module - python

--Conditional Executing
based on exit status
0 means success

if grep "127.0.0.1" /etc/hosts; then
    echo "everyting ok"
else
    echo "ERROR! 127.0.0.1 not in /etc/hosts"
fi

Test command - is a command that evaluates the conditions reveived and exits with zero when they are true
and with one when they are false
if test -n "$PATH"; then echo "Your path is not empty"; fi
if [ -n "$PATH" ]; then echo "Your path is not empty"; fi

--While loops 
n=0
command=$1
while ! $command && [ $n -le 5 ]; do
    sleep $n
    ((n+=1))
    echo "Retry #$n"
done;

--For Loops
for fruit in peach orange apple; do
    echo "I like $fruits!"
done

for file in *.HTM; do
    name=$(basename "$file" .HTM)
    mv "$file" "$name.html"
done

--FINAL LAB
cd data
cat list.txt
ls
grep 'jane' ../data/list.txt
grep ' jane ' ../data/list.txt
grep " jane " ../data/list.txt | cut -d ' ' -f 1
grep " jane " ../data/list.txt | cut -d ' ' -f 2
grep " jane " ../data/list.txt | cut -d ' ' -f 3
grep " jane " ../data/list.txt | cut -d ' ' -f 1-3
grep " jane " ../data/list.txt | cut -d ' ' -f 1,3
test EXPRESSION
if test -e ~/data/jane_profile_07272018.doc; then echo "File exists"; else echo "File doesn't exist"; fi
> test.txt
echo "I am appending text to this test file" >> test.txt
cat test.txt
for i in 1 2 3; do echo $i; done

cd ~/scripts
nano findJane.sh
#!/bin/bash
> oldFiles.txt
chmod +x findJane.sh
./findJane.sh
#!/bin/bash

files= grep ' jane ' ../data/list.txt | cut -d ' ' -f 3

for file in files; do

   if  test -e ~/data/$file; then
     echo  $file >> oldFiles.txt;
   else
     echo "File dosen't exsist"; fi
done

nano changeJane.py
#!/usr/bin/env python3
import sys
import subprocess
f= open (sys.argv[1],"r")
path='/home/<username>'
for line in f.readlines():
 old_name = line.strip()
 new_name = old_name.replace("jane","jdoe")
 subprocess.run(["mv",path+old_name,path+new_name])
f.close()


"""

