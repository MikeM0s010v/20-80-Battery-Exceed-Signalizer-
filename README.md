-20-80-Battery-Charge-Percentage-Exceed-Signalizer-
LINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUX
Roughly written venv-python alarm program for 20-80% battery rule. It simply reminds you to plug-unplug the power cable to lengthten the battery life.  The programme starts as you login into your Linux user account..

Steps to reproduce
1. Create venv folder. Put the python script and alarm wav-file in there.
2. Create a bash script that changes directory and runs the py-file.
3. Add modifications to your .bashrc-file.  

Enjoy! LOL


There is some time lag in python power_plugged attribute status updating. Thus some code refactoring and further sleeptime adjustments may be made, added or detalized.

CPU usage check:
ps aux --sort=-%mem | grep -i '[p]ython'
user 2300  0.0  0.0 256060 17720 pts/0    S+   04:21   0:00 python alert.py

Feel free to use, comment and play around with code!

