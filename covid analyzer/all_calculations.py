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
    measures_list = [measure.measure for measure in measures_dict]
    countries = [measure.countries_list for measure in measures_dict]
    measure_input = args.b
    required_index_2 = [i for i, e in enumerate(measures_list) if e == measure_input]
    countries_following_required_measure = []
    for i in required_index_2:
        countries_following_required_measure.append(countries[i])
    countries_following_required_measure = list(dict.fromkeys(countries_following_required_measure))
    print(countries_following_required_measure)

    cases_dict = FileReader().covid_cases_reader("covid_cases_stats.csv")
