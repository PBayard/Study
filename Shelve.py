import shelve, os # create persistent dic like object

crtPath = os.getcwd()
os.chdir(os.pardir)
crtPath = os.getcwd()
shelfFile = shelve.open('mydata') # pass a filename
cats = ['Zophie', 'Pooka', 'Simon'] # values as for a Dic
shelfFile['cats'] = cats
shelfFile.close() # creates in working directory mydata.bak, mydata.dat, and mydata.dir (windows)
# Shelf values don’t have to be opened in read or write mode

shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()) )
shelfFile.close()
