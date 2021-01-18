import csv

covid_cases_stats = csv.DictReader(open("covid_cases_stats.csv"))
covid_safety_measures = csv.DictReader(open("covid_safety_measures.csv"))
for line in covid_cases_stats:
    lines=dict(line)
    print(lines)
