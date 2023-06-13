#!/usr/bin/python3
# 4-from_json_string.py
"""This Module contains a function that  returns an object 
(Python data structure) represented by a JSON string
"""

import json


def from_json_string(my_str):
    """ Function that returns an object  repewswnted by a JSON representation

    Args:
        my_str: JSON representation

    Raises:
        Exceptions: None

    """
    return json.loads(my_str)
