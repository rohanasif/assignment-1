
import csv


def FileReader(path):
    fileread = csv.DictReader(open(path, encoding='utf-8'))
    data =[]
    for row in fileread:
        data.append(row)
    
    return data
