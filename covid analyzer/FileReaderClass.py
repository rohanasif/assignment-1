class FileReader:
    def cases_reader_1(self, file_path):
        cases_reader_1 = csv.DictReader(open(file_path))
        for row in cases_reader_1:
            c = row['country']
            print c

    def cases_reader_2(self,file_path):
        cases_reader_2 = csv.DictReader(open(file_path))
        for row in cases_reader_2:
            d = row['measure']



#class Country:
    def __init__(self, file_path, name, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases,\
     serious_critical_cases)
        self.file_path=file_path
        self.name = name
        self.total_cases = total_cases
        self.new_cases = new_cases
        self.total_deaths = total_deaths
        self.new_deaths = new_deaths
        self.total_recovered = total_recovered
        self.active_cases = active_cases
        self.serious_critical_cases = serious_critical_cases

