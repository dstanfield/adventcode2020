import csv

valuesString = []

with open('input.csv', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        valuesString.append(row[0])

values = [int(numeric_string) for numeric_string in valuesString]

print (values)

for year in values:
    for secondyear in values:
        for thirdyear in values:
            if year + secondyear + thirdyear == 2020:
                answer = year*secondyear*thirdyear
                print(str(year) + ' and ' + str(secondyear) + ' and ' + str(thirdyear) + ' add up to 2020 and multiply to ' + str(answer) )
