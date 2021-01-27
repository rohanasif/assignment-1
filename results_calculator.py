
from collections import Counter


class ResultsCalculator:
    # Part (a) calculations
    def recovered_over_total(self, args, cases_dict):
        recovered_cases = ([case.total_recovered for case in cases_dict])
        total_cases = ([case.total_cases for case in cases_dict])
        names = ([case.name for case in cases_dict])
        country_input = args.a
        print(country_input)
        required_index = names.index(country_input)
        required_ratio = int(recovered_cases[required_index])/int(total_cases[required_index])
        print("%.2f" % required_ratio)

    # Part (b) calculations
    def measures_death_rate(self, args, cases_dict, measures_dict):

        measures_list = [measure.measure for measure in measures_dict]  # list of all measures in the file
        countries = [measure.countries_list for measure in measures_dict]  # list of all countries in the file
        measure_input = args.b
        required_index = [i for i, e in enumerate(measures_list) if e == measure_input]  # list of indexes of countries \
        # following required measure
        countries_following_required_measure = []
        for i in required_index:
            countries_following_required_measure.append(countries[i])
        countries_following_required_measure = list(dict.fromkeys(countries_following_required_measure))  # remove\
        # duplicates
        total_cases = 0
        total_deaths = 0
        total_cases_in_each_country = ([int(case.total_cases) for case in cases_dict])
        total_deaths_in_each_country = ([case.total_deaths for case in cases_dict])
        for i in range(0, len(total_deaths_in_each_country)):  # loop to convert all string nums to int nums
            if total_deaths_in_each_country[i] == '':
                total_deaths_in_each_country[i] = '0'
            total_deaths_in_each_country[i] = int(total_deaths_in_each_country[i])
        names = ([case.name for case in cases_dict])
        print(len(total_cases_in_each_country))
        countries_index=[]
        for name in names:
            if name in countries_following_required_measure:
                countries_index.append(names.index(name))
        #print(countries_index)
        for index in countries_index:
            total_cases += total_cases_in_each_country[index]
            total_deaths += total_deaths_in_each_country[index]

        print(str((total_deaths/total_cases)*100) + "% death average found in " +
              (str(len(countries_following_required_measure))) + " countries")
