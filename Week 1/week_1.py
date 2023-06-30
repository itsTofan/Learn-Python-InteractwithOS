#Python Operation with OS
#Operation system is the software that manages everthing that goes on in the computer
#Kernel is the main core of OS, talk to hardware
#user space
#this course focus on manging files.
#Windows, mac os, linux
#linus distribution - ubuntu, debian, red hat
#unix develop by belllabs
#pyhton external module - PyPi python package index
#pip - command line tool - cross platform tools use to install, update and remove external module
#pip install requests to install external module dealing with web services

import requests
#ger function process website and response object has it content
#response = requests.get("http://www.google.com")
#print(len(response.text))

#interpreted language - python, ruby, javascript, bash, powershell 
#compiler translate a code to machine level language to specific underling os
#compile programming language c, c++, Go, Rust
#relly on intrepreter

#run python on linux command line
#python 3
#cat to show content of file cat hello_world.py
#pyhton3 hello_world.py - to run script
#shebang - command to use to execute script
#nano editior in linux
#!/user/bin/env python3
#make file executeable with CHMOD
#chmod +x hello_world.py
#run with ./hello_world.py


#---------------------------------------------------------
#---------------------------------------------------------
#python module - code reuse 
import areas
print(areas.triangle(3, 5))
print(areas.circle(4))

#benefit of automation -centralizing mistake
#pitfall of automation - trade off - is the time and effort of write script is worth potential automation benefits?
#time to automate < (time to perform * amount time done)
#pareto principle - 20% if the system administration task that you perform are responsible for 80% of your work.
#bit-rot is the process of software falling out of step with the environment
#automation example - check healths of computer
import shutil #disk usage
import psutil #cpu usage
#shebang - command to use to execute script
#nano editior in linux
#!/user/bin/env python3

#get disk usage
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

#check cpu usage
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR")
else:
    print("Everything is OK!")
