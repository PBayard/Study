#! /usr/bin/env python3
# RegexSearch.py
import re

RegexPattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = RegexPattern.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

RegexPattern = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = RegexPattern.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group(2))
print('Phone number found: ' + mo.group(1))
print('Phone number found: ' + mo.group(0))
print('Phone number found: ' + mo.group())
print(mo.groups())
areaCode, mainNumber = mo.groups()

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print('Indicatif: ' + mo.group(1))

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel batbat')
print(mo.group(1))
print(mo.group())

batRegex = re.compile(r'Bat(wo)?man')
batRegex = re.compile(r'Bat(wo)*man')
batRegex = re.compile(r'Bat(wo)+man')
haRegex = re.compile(r'(Ha){3}')
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)

xmasRegex = re.compile(r'\d+\s\w+') # cf. p158
atRegex = re.compile(r'.at')
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
newlineRegex = re.compile('.*', re.DOTALL)

robocop = re.compile(r'robocop', re.I) # Case-Insensitive Matching
mo = robocop.search('RoboCop is part man, part machine, all cop.').group()
print(mo)

namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo)

