import csv
import os
os.chdir('/home/pat/Documents/Dropbox/Info/PC/Python/PycharmProjects/automate_online-materials')
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)

for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

print('*****' * 10)
exampleFile = open('example.csv') # The Reader object can be looped over only once.
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)
print(exampleData[0][0]) # row col

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile) # csvWriter = csv.writer(outputFile, delimiter='\t', lineterminator='\n\n')
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()