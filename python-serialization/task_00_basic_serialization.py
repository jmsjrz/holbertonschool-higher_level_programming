#!/usr/bin/python3
"""Basic serialization."""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize the data to JSON and save it to the specified file.

    :param data: A Python Dictionary with data
    :param filename: The filename of the output JSON file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_and_deserialize(filename):
    """
    Load and deserialize data from the specified file.

    :param filename: The filename of the input JSON file
    :return: A Python Dictionary with the deserialized JSON data
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
