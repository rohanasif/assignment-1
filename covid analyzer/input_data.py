import csv
line = []
input_file = csv.DictReader(open("covid_safety_measures.csv"))

for line in input_file:
    print(line)
