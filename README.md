-20-80-Battery-Charge-Percentage-Exceed-Signalizer-
Refactoring!
LINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUXLinux
Elegantly written venv-python alarm for 20-80% battery rule. It simply reminds you to plug-unplug the power cable to lengthten the battery life. The program starts at boot as you login into your user account..

Steps to reproduce
1. Create venv folder.
2. Download wav-alarm-file that you like fron web.
3. Create/copy a python file.
4. Create/copy a bash script that will run the python file.
5. Make it executable.
6. Put aforementioned files in your venv folder.
7. Create a new 'at' entry.
 
Enjoy! LOL


There is some time lag in python power_plugged attribute status updating. Thus, some code refactoring and further sleeptime adjustments may be made, added or detalized.

CPU usage check:
ps aux --sort=-%mem | grep -i '[p]ython'
user 2300  0.0  0.0 256060 17720 pts/0    S+   04:21   0:00 python alert.py

System requirements: Linux arch 6.6.3-arch1-1, python 3.11.6, at service running

============================
Feel free to use, comment and play around with code!

P.S. I could't find any sort of such software. So, I wanted to create one on my own. It is a skill training soft written fast. Still it works! 

  
