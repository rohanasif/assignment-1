class FileReader:
    def cases_reader_1(self, file_path):
        cases_reader_1 = csv.DictReader(open(file_path))
        for row in cases_reader_1:
            c = row['country']
    def cases_reader_2(self,file_path):
        cases_reader_2 = csv.DictReader(open(file_path))
        for row in cases_reader_2:
            d = row['measure']