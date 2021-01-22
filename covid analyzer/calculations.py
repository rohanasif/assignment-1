import argparse
from FileReader import FileReader

# Part (a) calculations
def part_a():
    cases_dict = FileReader().covid_cases_reader("covid_cases_stats.csv")
    recovered_cases = ([case.total_recovered for case in cases_dict])
    total_cases = ([case.total_cases for case in cases_dict])
    names = ([case.name for case in cases_dict])
    country_input = args.a
    print(country_input)
    required_index = names.index(country_input)
    required_ratio = int(recovered_cases[required_index])/int(total_cases[required_index])
    print("%.2f" % required_ratio)

