import csv
import argparse

# Create the parser
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('-b', type=str, required=True)
# Parse the argument
args = parser.parse_args()

input_file = csv.DictReader(open("covid_safety_measures.csv"))
for row in input_file:
    c = row['category']
    if c == args.b:
        print(c)
