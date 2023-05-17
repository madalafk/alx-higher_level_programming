0. Squared simple
This function computes the square value of all integers of a matrix.
•	Prototype used : def square_matrix_simple(matrix=[]):
•	matrix is a 2 dimensional array
•	Returns a new matrix:
o	Same size as matrix
o	Each value should be the square of the value of the input
•	Initial matrix should not be modified
•	not allowed to import any module
•	using regular loops, map, etc.

1. Search and replace
This function that replaces all occurrences of an element by another in a new list.
•	Prototype used: def search_replace(my_list, search, replace):
•	my_list is the initial list
•	search is the element to replace in the list
•	replace is the new element
•	not allowed to import any module
2. Unique addition
This function adds all unique integers in a list (only once for each integer).
•	Prototype used: def uniq_add(my_list=[]):
•	not allowed to import any module
3. Present in both
This function returns a set of common elements in two sets.
•	Prototype used: def common_elements(set_1, set_2):
•	not allowed to import any module
4. Only differents
This function returns a set of all elements present in only one set.
•	Prototype used: def only_diff_elements(set_1, set_2):
•	not allowed to import any module
5. Number of keys
This  function returns the number of keys in a dictionary.
•	Prototype used: def number_keys(a_dictionary):
•	Not allowed to import any module
6. Print sorted dictionary
This function prints a dictionary by ordered keys.
•	Prototype used: def print_sorted_dictionary(a_dictionary):
•	assumes that all keys are strings
•	Keys sorted by alphabetic order
•	Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
•	Dictionary values can have any type
•	Not allowed to import any module
7. Update dictionary
This function replaces or adds key/value in a dictionary.
•	Prototype used: def update_dictionary(a_dictionary, key, value):
•	key argument will be always a string
•	value argument will be any type
•	If a key exists in the dictionary, the value will be replaced
•	If a key doesn’t exist in the dictionary, it will be created
•	not allowed to import any module
8. Simple delete by key
This function deletes a key in a dictionary.
•	Prototype used: def simple_delete(a_dictionary, key=""):
•	key argument will be always a string
•	If a key doesn’t exist, the dictionary won’t change
•	not allowed to import any module
9. Multiply by 2
This  function returns a new dictionary with all values multiplied by 2
•	Prototype used: def multiply_by_2(a_dictionary):
•	assumes that all values are only integers
•	Returns a new dictionary
•	not allowed to import any module
10. Best score

This function returns a key with the biggest integer value.
•	Prototype used: def best_score(a_dictionary):
•	assumes that all values are only integers
•	If no score found, return None
•	assumes all students have a different score
•	not allowed to import any module
11. Multiply by using map
This function returns a list with all values multiplied by a number without using any loops.
•	Prototype used: def multiply_list_map(my_list=[], number=0):
•	Returns a new list:
o	Same length as my_list
o	Each value is multiplied by number
•	Initial list is not modified
•	not allowed to import any module
•	used map
•	file with max 3 lines
12. Roman to Integer
Technical interview preparation:
•	not allowed to google anything
•	used Whiteboard first
a function def roman_to_int(roman_string): that converts a Roman numeral to an integer.
•	assumes the number will be between 1 to 3999.
•	def roman_to_int(roman_string) must return an integer
•	If the roman_string is not a string or None, return 0
13. Weighted average!
This  function returns the weighted average of all integers tuple (<score>, <weight>)
•	Prototype used: def weight_average(my_list=[]):
•	Returns 0 if the list is empty
•	not allowed to import any module
14. Squared by using map
This  function computes the square value of all integers of a matrix using map
•	Prototype used : def square_matrix_map(matrix=[]):
•	matrix is a 2 dimensional array
•	Returns a new matrix:
o	Same size as matrix
o	Each value is the square of the value of the input
•	Initial matrix is not modified
•	not allowed to import any module
•	used map
•	not allowed to use for or while
•	file is max 3 lines
15. Delete by value
This function deletes keys with a specific value in a dictionary.
•	Prototype used: def complex_delete(a_dictionary, value):
•	If the value doesn’t exist, the dictionary won’t change
•	All keys having the searched value are deleted
•	not allowed to import any module


16. CPython #1: PyBytesObject
#advanced
Create two C functions that print some basic info about Python lists and Python bytes objects.

Python lists:
•	Prototype used: void print_python_list(PyObject *p);

Python bytes:
•	Prototype8 used: void print_python_bytes(PyObject *p);
•	Format: see example
•	Line “first X bytes”: print a maximum of 10 bytes
•	If p is not a valid PyBytesObject, print an error message (see example)
•	Read /usr/include/python3.4/bytesobject.h
About:
•	Python version: 3.4
•	shared library is compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
•	not allowed to use the following macros/functions:
o	Py_SIZE
o	Py_TYPE
o	PyList_GetItem
o	PyBytes_AS_STRING
o	PyBytes_GET_SIZE

