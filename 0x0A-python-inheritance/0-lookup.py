#!/usr/bin/python3
# 0-lookup.py
"""This module Defines an object attribute lookup."""

def lookup(obj):
    """Returns (list of an object's available attributes.)"""
    return dir(obj)
