import subprocess

# subprocess.Popen('C:\\Windows\\System32\\calc.exe')
calcProc = subprocess.Popen('/usr/bin/gnome-calculator')
calcProc.poll() == None
calcProc.wait()
calcProc.poll()
subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\hello.txt'])

# Task Scheduler on Windows,
# launchd on OS X, or the cron scheduler on Linux (crontab -e)

subprocess.Popen(['C:\\python34\\python.exe', 'hello.py'])
# The location of the Python executable on Windows is C:\python34\python
# .exe. On OS X, it is /Library/Frameworks/Python.framework/Versions/3.3/bin/
# python3. On Linux, it is /usr/bin/python3

subprocess.Popen(['start', 'hello.txt'], shell=True)
# On Windows, this is the start
# program. On OS X, this is the open program. On Ubuntu Linux, this is the
# see program.