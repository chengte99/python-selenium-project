import csv

data = csv.reader(open('info.csv', 'r'))

for info in data:
    print(info)
