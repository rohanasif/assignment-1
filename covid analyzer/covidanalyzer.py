import argparse
from calculations import part_a



# Create the parser
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('-a', type=str, required=True)
# Parse the argument
args = parser.parse_args()

part_a()

measures_dict = FileReader().covid_measures_reader("covid_safety_measures.csv")
print([measure.measure for measure in measures_dict])


# task 1: For a given country, display the ratio of recovered patients over total cases.
# commandline input: covidanalyzer.py /path/to/files-dir -a "Pakistan"
# output: Recovered/total ratio: 0.23
# We have the data in the covid_case_stats.xlx file about recovered vs total so we can find the ratio from there.

# task 2: For a given safety measure, display the average death rate around the globe.
# commandline input: covidanalyzer.py /path/to/files-dir -b "Economic measures"
# output: 43.28% death average found in 89 countries.
# calculate the ratio of total deaths of all countries following the measure and the total cases of all such countries

# task 3: Display the efficiencies of 5 mostly adopted safety measures. The efficiency can be calculated as
# efficiency = total recovered cases of all countries taken the measure / total cases of all countries taken the measure
# commandline input: covidanalyzer.py /path/to/files-dir -c
# output: Economic measures: 0.47
#         Limit public gatherings: 0.42
#         Introduction of quarantine policies: 0.53
#         Strengthening the public health system: 0.48
#         International flights suspension: 0.36
#         graph of the four outputs
