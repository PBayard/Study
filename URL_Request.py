import requests
# res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
    
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))