import argparse
from covidanalyzer import part_a

# Create the parser
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('-a', type=str, required=True)
# Parse the argument
args = parser.parse_args()

part_a()
