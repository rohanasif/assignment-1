import csv


class FileReader:
    import csv
    def covid_cases_reader(self, file_path):
        covid_cases_reader = csv.DictReader(open(file_path))
        lines = []
        for row in covid_cases_reader:
            country = Country(row['country'], row['total_cases'], row['new_cases'], row['total_deaths'],
                            row['new_deaths'], row['total_recovered'], row['active_cases'],
                            row['serious_critical_cases'])
            lines.append(country)
        return lines

class Country:
    def __init__(self, name, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases,serious_critical_cases):

        self.name = name
        self.total_cases = total_cases
        self.new_cases = new_cases
        self.total_deaths = total_deaths
        self.new_deaths = new_deaths
        self.total_recovered = total_recovered
        self.active_cases = active_cases
        self.serious_critical_cases = serious_critical_cases
