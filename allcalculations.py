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
    data1 = FileReader().covid_cases_reader('covid_cases_stats.csv')
    data2 = FileReader().covid_measures_reader('covid_safety_measures.csv')
    countries = []
    for row in data2:
        if data2.measure == args.b:
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
    print((total_deaths / total_cases) * 100)
