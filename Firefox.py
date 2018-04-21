import subprocess

ls_output = subprocess.call('ls')
#  test = subprocess.run(firefox)
subprocess.call('ls -l', shell=True)
# subprocess.call('firefox http://www.google.com', shell=True)
subprocess.run('firefox http://rezo.net', shell=True)





