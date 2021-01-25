
import FileReader
from collections import Counter


def recovered_over_total(args_country):
    data1 = FileReader.FileReader('covid_cases_stats.csv')
    country_input = args_country
    print(country_input)
    for row in data1:
        if row['country'] == country_input:
            print("%.2f" % (int(row['total_recovered'])/int(row['total_cases'])))


def measures_death_rate(args_measure):
    data1 = FileReader.FileReader('covid_cases_stats.csv')
    data2 = FileReader.FileReader('covid_safety_measures.csv')
    countries = []
    for row in data2:
        if row['measure'] == args_measure:
            countries.append(row['country'])
    countries = list(dict.fromkeys(countries))
    total_cases = 0
    total_deaths = 0
    
    for country in countries:
        for row in data1:
            if country == row['country'] and row['total_deaths']:
                total_cases += int(row['total_cases'])
                total_deaths += int(row['total_deaths'])
                break
    print(("%.2f" % ((total_deaths/total_cases)*100))+"% death average found in " + str(len(countries)) + " countries")


def efficiencies():
    data1 = FileReader.FileReader('covid_cases_stats.csv')
    data2 = FileReader.FileReader('covid_safety_measures.csv')
    measures = []
    for row in data2:
        measures.append(row['measure'])
    ocurrences = Counter(measures)
    mc = ocurrences.most_common(5)
    new = []
    for row in mc:
        new.append(row[0])
    
    for item in new:
        countries1 = []
        for row in data2:
            if row['measure'] == item:
                countries1.append(row['country'])
                
        countries1 = list(dict.fromkeys(countries1))
        total_cases = 0
        total_recovered = 0
        
        for country in countries1:
            for row in data1:
                if country == row['country'] and row['total_recovered']:
                    total_cases += int(row['total_cases'])
                    total_recovered += int(row['total_recovered'])
                    break
        
        efficiency = total_recovered/total_cases
        print(item, "%.2f" % efficiency)
