#!/usr/bin/python3
"""Convert a Python object to an XML string."""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML and save it to the given filename.

    :param dictionary: The dictionary to serialize
    :param filename: The filename to save the serialized XML data
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Deserialize XML data from the given filename into a Python dictionary.

    :param filename: The filename to read the XML data from
    :return: A dictionary with the deserialized data
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        deserialized_data = {}
        for child in root:
            deserialized_data[child.tag] = child.text

        return deserialized_data
    except Exception as e:
        print(f"Error: {e}")
        return None
