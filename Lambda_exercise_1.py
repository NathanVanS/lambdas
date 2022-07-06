import csv
from functools import reduce

def getInfo():
    the_report = []

    #with open('Calls.csv') as file:
    with open('C:\Users\Nathaniel\Documents\Dev10\OODM\Calls.csv') as file:
        reader = csv.reader(file)

    first_row = True
    headers = []

    for row in reader:
        if first_row:
            headers = row
            first_row = False

        else:
            data = {}
            for a in range(len(headers)):                    
                data[headers[a]] = row[a]
                the_report.append(data)

    return the_report

def lambders():
    the_report = getInfo()
   
    the_report = list(filter(lambda x: x['zip_code'] != '', the_report))
    the_report = list(filter(lambda x: x['neighborhood'] != '', the_report))
    the_report = list(filter(lambda x: x['totalresponsetime'] != '', the_report))

    sumtrt = reduce(sum, the_report['totalresponsetime'])
    print(sumtrt)


lambders()