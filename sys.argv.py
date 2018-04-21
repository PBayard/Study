#! /usr/bin/env python3
# sys.argv.py - An insecure password locker program.
import sys

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python sys.argv.py [account] - copy account password')
    sys.exit()

if sys.argv[1] in PASSWORDS:
    sys.argv[1].copy(PASSWORDS[sys.argv[1]])
    print('Password for ' + sys.argv[1] + ' copied to clipboard.')
else:
    print('There is no account named ' + sys.argv[1])

print ("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: " , str(sys.argv))