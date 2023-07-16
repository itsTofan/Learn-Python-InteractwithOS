"""
--FINAL PROJECT

- Writing script from ground up
1. Understand the problem
2. Research
3. Planning
4. Writing the code

--Project Problem Statement
Produce report from syslog

Imagine your company uses a server that runs a service called ticky, an internal ticketing system. The service logs events to syslog, both when it runs successfully and when it encounters errors.

The service's developers need your help getting some information from those logs so that they can better understand how their software is used and how to improve it. So, for this lab, you'll write some automation scripts that will process the system log and generate reports based on the information extracted from the log files.

What you'll do
Use regex to parse a log file
Append and modify values in a dictionary
Write to a file in CSV format
Move files to the appropriate directory for use with the CSV->HTML converter
You'll have 90 minutes to complete this lab.

cat syslog.log
grep ticky syslog.log
grep "ERROR" syslog.log
grep "ERROR Tried to add information to closed ticket" syslog.log

python3
import re
line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
re.search(r"ticky: INFO: ([\w ]*) ", line)
line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
re.search(r"ticky: ERROR: ([\w ]*) ", line)

fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
sorted(fruit.items())
import operator
sorted(fruit.items(), key=operator.itemgetter(0))
sorted(fruit.items(), key=operator.itemgetter(1))
sorted(fruit.items(), key = operator.itemgetter(1), reverse=True)

nano user_emails.csv

Full Name, Email Address
Blossom Gill, blossom@abc.edu
Hayes Delgado, nonummy@utnisia.com
Petra Jones, ac@abc.edu
Oleg Noel, noel@liberomauris.ca
Ahmed Miller, ahmed.miller@nequenonquam.co.uk
Macaulay Douglas, mdouglas@abc.edu
Aurora Grant, enim.non@abc.edu
Madison Mcintosh, mcintosh@nisiaenean.net
Montana Powell, montanap@semmagna.org
Rogan Robinson, rr.robinson@abc.edu
Simon Rivera, sri@abc.edu
Benedict Pacheco, bpacheco@abc.edu
Maisie Hendrix, mai.hendrix@abc.edu
Xaviera Gould, xlg@utnisia.net
Oren Rollins, oren@semmagna.com
Flavia Santiago, flavia@utnisia.net
Jackson Owens, jackowens@abc.edu
Britanni Humphrey, britanni@ut.net
Kirk Nixon, kirknixon@abc.edu
Bree Campbell, breee@utnisia.net

sudo chmod +x csv_to_html.py
sudo chmod  o+w /var/www/html
./csv_to_html.py user_emails.csv /var/www/html/report1.html


"""