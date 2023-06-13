#!/usr/bin/python3
# 5-save_to_json_file.py

""" This Module has function that writes an Object to a text file,
	using a JSON representation
"""
import json


def load_from_json_file(filename):
    """ Function that creates an Object from a JSON file

    Args:
        filename:name for the file used

    Raises:
        Exception: None

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
