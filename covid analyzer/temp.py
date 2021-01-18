import csv

covid_cases_reader = csv.DictReader(open("covid_cases_stats.csv"))
lines=[]
for row in covid_cases_reader:
    lines.append(dict(row))
return lines