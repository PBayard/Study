#! python3
import os
import locale
locale.setlocale(locale.LC_ALL, '')  # use user's preferred locale

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(locale.format('%d', totalSize, 1))

print('{:d}'.format(totalSize)) # d = integer
print('{:f}'.format(totalSize)) # f = float
print('{:.2f}'.format(totalSize)) # f = float 2 decimals
print('{:+d}'.format(totalSize))
print('{:+d}'.format(totalSize))
print('{:,d}'.format(totalSize)) # comma separated
print('{:d}'.format(totalSize))
print('{:.2%}'.format(0.2)) # percentages
