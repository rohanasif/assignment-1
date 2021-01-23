import argparse
from FileReader import FileReader

# Part (a) calculations
def recovered_over_total(args):
    cases_dict = FileReader().covid_cases_reader("covid_cases_stats.csv")
    recovered_cases = ([case.total_recovered for case in cases_dict])
    total_cases = ([case.total_cases for case in cases_dict])
    names = ([case.name for case in cases_dict])
    country_input = args.a
    print(country_input)
    required_index = names.index(country_input)
    required_ratio = int(recovered_cases[required_index])/int(total_cases[required_index])
    print("%.2f" % required_ratio)

# Part (b) calculations
def measures_death_rate(args):
    measures_dict = FileReader().covid_measures_reader("covid_safety_measures.csv")
    measures_list = [measure.measure for measure in measures_dict]  # list of all measures in the file
    countries = [measure.countries_list for measure in measures_dict]  # list of all countries in the file
    measure_input = args.b
    required_index_2 = [i for i, e in enumerate(measures_list) if e == measure_input]  # list of indexes of countries \
    # following required measure
    countries_following_required_measure = []
    for i in required_index_2:
        countries_following_required_measure.append(countries[i])
    countries_following_required_measure = list(dict.fromkeys(countries_following_required_measure))  # remove\
    # duplicates
    # print(len(countries_following_required_measure))
    # print(countries_following_required_measure)
    # print(len(countries_following_required_measure))
    cases_dict = FileReader().covid_cases_reader("covid_cases_stats.csv")
    total_cases = 0
    total_deaths = 0
    total_cases_in_country = ([int(case.total_cases) for case in cases_dict])
    # print(total_cases_in_country)
    # print(len(total_cases_in_country))
    total_deaths_in_country = ([case.total_deaths for case in cases_dict])
    for i in range(0, len(total_deaths_in_country)):  # loop to convert all string nums to int nums
        if total_deaths_in_country[i] == '':
            total_deaths_in_country[i] = '0'
        total_deaths_in_country[i] = int(total_deaths_in_country[i])
    # print(total_deaths_in_country)
    # print(len(total_deaths_in_country))
    # print(sum(total_cases_in_country))
    # print(sum(total_deaths_in_country))
    # for country in countries_following_required_measure:
        # total_cases += total_cases_in_country
        # total_deaths += total_deaths_in_country
