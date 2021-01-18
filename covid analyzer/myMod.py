# -*- coding: utf-8 -*-

import csv
from collections import Counter
from pprint import pprint

path1 = "covid_cases_stats.csv"
path2 = "covid_safety_measures.csv"


def readCsvFile(path):  # read csv file into dictionary
    input_file = csv.DictReader(open(path, encoding='utf-8'))
    return input_file


def country(country):  # return 'total_recovered' and 'total_cases' of given country
    file = readCsvFile(path1)
    for row in file:
        c = row['country']
        if c == country and row['total_recovered']:
            return int(row['total_recovered']), int(row['total_cases'])


def ratio(countr):  # calculates ratio
    recovered, total = country(countr)
    return (recovered / total)


def countriesMeasure(measure):  # Return list of countries who took given measure
    file = readCsvFile(path2)
    countries = []
    for row1 in file:
        d = row1['measure']
        if d == measure:
            countries.append(row1['country'])
    countries = list(dict.fromkeys(countries))
    return countries


def deathRate(countries):  # calculate death rate
    file = readCsvFile(path1)
    tot_cases = 0
    tot_deaths = 0
    for row in file:
        for cnt in countries:
            if row['country'] == cnt and row['total_deaths']:  # check for non-empty value
                tot_deaths += int(row['total_deaths'])
                tot_cases += int(row['total_cases'])
    return (tot_deaths / tot_cases) * 100


def measures():  # returns all measures in csv file
    file = readCsvFile(path2)
    measures = []
    for row1 in file:
        d = row1['measure']
        measures.append(d)
    return measures


def frequent():  # return frequent measures
    occurence_count = Counter(measures())
    res = occurence_count.most_common(5)
    cl = []
    for i in res:
        cl.append(i[0])
    return cl


def efficiency(measure):  # calculate efficiency
    cont = countriesMeasure(measure)
    total_recov = 0
    total_cas = 0
    for c in cont:
        if(country(c)):  # check if not empty
            total_r, total_c = country(c)
            total_recov += total_r
            total_cas += total_c
    return total_recov / total_cas


def printEfficiency():
    for a in frequent():
        print(a, "%.2f" % efficiency(a))
