import csv
exampleFile = open('ixchariot.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData[5][4])

