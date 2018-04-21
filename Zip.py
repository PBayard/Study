#!/usr/bin/python3
import zipfile, os

os.chdir('/home/pat/Documents/utilit/Temp')
# move to the folder with lpdp.zip
exampleZip = zipfile.ZipFile('LPDP.zip')
print(exampleZip.namelist())
spamInfo = exampleZip.getinfo('img_0403.jpg')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
#exampleZip.extractall()
#exampleZip.extract('img_0403.jpg', 'C:\\some\\new\\folders')
newZip = zipfile.ZipFile('new.zip', 'w')  # or 'a' to append
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
exampleZip.close()