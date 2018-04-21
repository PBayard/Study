cat = ['fat', 'black', 'loud']
size, color, disposition = cat
print(size)

print(cat.index('loud')) # If the value appears multiple times in the list,
# only the first instance

cat.append('moose')
print(cat)

cat.insert(0,'cow')
print(cat)

cat.remove('black') # If the value appears multiple times in the list,
# only the first instance of the value will be removed
print(cat)

spam = [['cat', 'bat'], [10, 20, 30, 40, 50],['Hop', 'bof']]
print(spam[0][1]) # first list, second item in list
print(spam[1][4])
print(spam[2][0])
del spam[1]
print(spam)

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)

spam = ['a', 'z', 'A', 'Z'] # uppercase letters come before lower-case letters
spam.sort()
print(spam)
spam.sort(key=str.lower)
print(spam)

import random

messages = ['It is certain',
'It is decidedly so',
'Yes definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful']
print(messages[random.randint(0, len(messages) - 1)])

# tuple is immutable hence faster, list is mutable with append, insert
print(tuple(['cat', 'dog', 5])) # convert list to tuple
print(list(('cat', 'dog', 5)))  # convert tuple to list