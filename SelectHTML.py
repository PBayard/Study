import requests, bs4

res = requests.get('https://rezo.net/')
res.raise_for_status()
# soup = bs4.BeautifulSoup(res.text, "lxml") # for ubuntu
soup = bs4.BeautifulSoup(res.text)
elems = soup.select('div')
print(str(elems[11]))
print(elems[11].getText())
elems = soup.select('#citation') # div id='citations'
print(len(elems))
print(elems[0].getText())
print(elems[0].attrs)