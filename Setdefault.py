message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0) # If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.
    count[character] = count[character] + 1
    print(count)