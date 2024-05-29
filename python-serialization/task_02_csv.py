#!/usr/bin/python3
"""Read a CSV file."""


import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format and write to data.json file.

    :param csv_filename: The filename of the input CSV file
    :return: True if the conversion was successful, False otherwise
    """
    try:
        # Open and read the CSV file
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        # Serialize the list of dictionaries to JSON
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
