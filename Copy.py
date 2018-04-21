#!/usr/bin/python
import os, shutil

path = "/home/pat/Documents/utilit/Temp/"

# Check current working directory.
retval = os.getcwd()
print ("Current working directory %s" % retval)

# Now change the directory
os.chdir( path )

# Check current working directory.
retval = os.getcwd()

print ("Directory changed successfully %s" % retval)

shutil.copy("/home/pat/Documents/utilit/Temp/test.txt", "/home/pat/Documents/utilit/Temp/test/")
shutil.copy("eggs.txt", "/home/pat/Documents/utilit/Temp/test/eggs2.txt")  # Casse important. Overwrite without problem
shutil.copytree('/home/pat/Documents/utilit/Temp/', '/home/pat/Documents/utilit/test/')  # whole, no overwrite
shutil.move('C:\\bacon.txt', 'C:\\eggs')
shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
shutil.move('C:\\bacon.txt', 'C:\\eggs')  # = rename

# delete
for filename in os.listdir():
    if filename.endswith('.rxt'):
        #os.unlink(filename)
        #os.rmdir(path)
        #shutil.rmtree(path)
        print(filename)

#import send2trash
#send2trash.send2trash('bacon.txt')
#N.B. cannot pull files out of it