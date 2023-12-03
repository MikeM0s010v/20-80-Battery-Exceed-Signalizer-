-20-80-Battery-Charge-Percentage-Exceed-Signalizer-
LINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUXLINUX
Elegantly written venv-python alarm for 20-80% battery rule. It simply reminds you to plug-unplug the power cable to lengthten the battery life. The program starts at boot as you login into your user account..

If any questions contact me:
IG mosolov_science
E-mail mosolov.mikhail@internet.ru

Steps to reproduce
1. Create virtual enviroment within YOUR venv folder with shell command 'virtualenv venv' (make sure if virualenv was previously installed with pip).
2. Download wav-alarm-file that you like fron web.
3. Create/copy a python file.
4. Optional (see 7). Create/copy a bash script that will run the python file (if you prefer 'at' service).
5. Also optional. Make it executable.
6. Put aforementioned files in YOUR venv folder (convinient step).

Full or partian automation:
7 . You are able to stop here and execute .py file whenever you want. 
Full-automation: Run the script with 'at' command (semi_automation) or add 'at -f /path/to/your.sh now' line to your /home/YOUuser/.bashrc file to executing program in the background right after boot. 
Full-automation invisible mode: implement cron  with new entry: crontab -e opens with vim, insert line '@reboot cd /path/to/your/venv/ && source bin/activate && XDG_RUNTIME_DIR=/run/user/$(id -u) bin/python alarm.py

Enjoy! 

CPU-usage check:
ps aux --sort=-%mem | grep -i '[p]ython'
user 2300  0.0  0.0 256060 17720 pts/0    S+   04:21   0:00 python alert.py

System requirements: Linux arch 6.6.3-arch1-1, python 3.11.6, 'at' or 'cronie' service running 

============================
Feel free to use, comment and play around with code!

P.S. I could't find any sort of such software. So, I wanted to create one on my own. It is a skill training soft written fast. Still it works! 

  
