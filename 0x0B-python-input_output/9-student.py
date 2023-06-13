#!/usr/bin/python3
# 11-student.py

"""This module contains  a class Student that defines a student.
"""


class Student:
    """Represent a class (student)."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dict representation of the Student."""
        return self.
