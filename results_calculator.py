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
        required_index = [i for i, e in enumerate(measures_list) if e == measure_input]  # list of indexes of countries\
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
        countries_index=[]
        for name in names:  # loop to get indexes of countries_follwing_required_measure in stats file
            if name in countries_following_required_measure:
                countries_index.append(names.index(name))
        # print(countries_index)
        for index in countries_index:
            total_cases += total_cases_in_each_country[index]
            total_deaths += total_deaths_in_each_country[index]

        print(str("%.2f" %((total_deaths/total_cases)*100)) + "% death average found in " +
              (str(len(countries_following_required_measure))) + " countries")

    # Part (c) calculations:
    def most_common_efficiencies(self, args, cases_dict, measures_dict):
        measures_list = [measure.measure for measure in measures_dict]
        countries = [measure.countries_list for measure in measures_dict]
        occurences = Counter(measures_list)
        most_common_dict = occurences.most_common(5)
        most_common_measures = []
        for row in most_common_dict:
            most_common_measures.append(row[0])
        for measure in most_common_measures:
            required_index = [i for i, e in enumerate(measures_list) if
                              e == measure]  # list of indexes of countries\
            # following required measure
            countries_following_required_measure = []
            for i in required_index:
                countries_following_required_measure.append(countries[i])
            countries_following_required_measure = list(dict.fromkeys(countries_following_required_measure))  # remove\
            # duplicates
            total_cases = 0
            total_recovered = 0
            total_cases_in_each_country = ([int(case.total_cases) for case in cases_dict])
            total_recovered_in_each_country = ([case.total_recovered for case in cases_dict])
            for i in range(0, len(total_recovered_in_each_country)):  # loop to convert all string nums to int nums
                if total_recovered_in_each_country[i] == '':
                    total_recovered_in_each_country[i] = '0'
                total_recovered_in_each_country[i] = int(total_recovered_in_each_country[i])
            names = ([case.name for case in cases_dict])
            countries_index = []
            for name in names:  # loop to get indexes of countries_follwing_required_measure in stats file
                if name in countries_following_required_measure:
                    countries_index.append(names.index(name))
            # print(countries_index)
            for index in countries_index:
                total_cases += total_cases_in_each_country[index]
                total_recovered += total_recovered_in_each_country[index]

            print(measure + ": " + str("%.2f" %(total_recovered/total_cases)))