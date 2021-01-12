import csv

input_file = csv.DictReader(open("covid_cases_stats.csv"))

for line in input_file:
    print(line)
