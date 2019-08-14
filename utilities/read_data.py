import csv

def getCsvData(filename):
    rows = []
    data = open(filename, "r")
    reader = csv.reader(data)
    next(reader)
    for row in reader:
        rows.append(row)
    return rows
