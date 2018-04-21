
import pprint
import sys

helloFile = open('Hello.txt') # Attn: Majuscule compte
print(helloFile.read())
print(helloFile.readlines()) # file pointer is positioned at the end of the file = returns []
helloFile.seek(0)  # bring file pointer at beginning
print(helloFile.readlines())

baconFile = open('bacon.txt', 'w') # write
baconFile.write('Hello world!\n')
baconFile.close()
baconFile = open('bacon.txt', 'a') # append
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

