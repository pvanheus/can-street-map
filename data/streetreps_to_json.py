import argparse
import csv
import json
import sys

def csv_to_json(input_file, output_file):
    csv_reader = csv.reader(input_file)

    header = next(csv_reader)
    keys = []
    for column in header:
        keys.append(column)
    
    data = []
    for row in csv_reader:
        element = {}
        for i, value in enumerate(row):
            element[keys[i]] = value
        data.append(element)
    
    json.dump(data, output_file, indent=2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert CSV file of Street Reps to JSON')
    parser.add_argument('input_file', type=argparse.FileType(), help='CSV file')
    parser.add_argument('output_file', nargs='?', default=sys.stdout, type=argparse.FileType('w'), help='JSON')
    args = parser.parse_args()

    csv_to_json(args.input_file, args.output_file)