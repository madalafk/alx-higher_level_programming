
0x0B. Python - Input/Output
Python

Learning Objectives
I have learnt the below lessons In this project:

•	How to open a file
•	How to write text in a file
•	How to read the full content of a file
•	How to read a file line by line
•	How to move the cursor in a file
•	How to make sure a file is closed after using it
•	What is and how to use the with statement
•	What is JSON
•	What serialization is
•	What deserialization is
•	How to convert a Python data structure to a JSON string
•	How to convert a JSON string to a Python data structure

Requirements
Python Scripts
•	Allowed editors: vi, vim, emacs
•	All files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
•	All files ends with a new line
•	The first line of all files is exactly #!/usr/bin/python3
•	Mandatory README.md file, at the root of the folder of the project
•	Code uses the pycodestyle (version 2.8.*)
•	All files are executable
•	The length of all files to be tested using wc
Python Test Cases
•	Allowed editors: vi, vim, emacs
•	All files ends with a new line
•	All test files are inside a folder tests
•	All test files are text files (extension: .txt)
•	All tests are executed by using this command: python3 -m doctest ./tests/*
•	All modules have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
•	All classes have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
•	All functions (inside and outside a class) have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')


Tasks
0. Read file
Write a function that reads a text file (UTF8) and prints it to stdout:
•	Prototype: def read_file(filename=""):
•	You must use the with statement
•	No need to manage file permission or file doesn't exist exceptions.
•	Not allowed to import any module
No test cases needed

1. Write to a file
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:
•	Prototype: def write_file(filename="", text=""):
•	Used the with statement
•	No need to manage file permission exceptions.
•	The function creates the file if doesn’t exist.
•	The function overwrites the content of the file if it already exists.
•	Not allowed to import any module
No test cases needed

2. Append to a file
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:
•	Prototype: def append_write(filename="", text=""):
•	If the file doesn’t exist, it should be created
•	Used the with statement
•	No need to manage file permission or file doesn't exist exceptions.
•	Not allowed to import any module
No test cases needed

3. To JSON string
Write a function that returns the JSON representation of an object (string):
•	Prototype: def to_json_string(my_obj):
•	No need to manage exceptions if the object can’t be serialized.
No test cases needed

4. From JSON string to Object
Write a function that returns an object (Python data structure) represented by a JSON string:
•	Prototype: def from_json_string(my_str):
•	No need to manage exceptions if the JSON string doesn’t represent an object.
No test cases needed


5. Save Object to a file
Write a function that writes an Object to a text file, using a JSON representation:
•	Prototype: def save_to_json_file(my_obj, filename):
•	Used the with statement
•	No need to manage exceptions if the object can’t be serialized.
•	No need to manage file permission exceptions.
No test cases needed

6. Create object from a JSON file
Write a function that creates an Object from a “JSON file”:
•	Prototype: def load_from_json_file(filename):
•	Used the with statement
•	No need to manage exceptions if the JSON string doesn’t represent an object.
•	No need to manage file permissions / exceptions.
No test cases needed

7. Load, add, save
Write a script that adds all arguments to a Python list, and then save them to a file:
•	Used function save_to_json_file from 5-save_to_json_file.py
•	Used function load_from_json_file from 6-load_from_json_file.py
•	The list saved as a JSON representation in a file named add_item.json
•	If the file doesn’t exist, it should be created
•	No need to manage file permissions / exceptions.
No test cases needed

8. Class to JSON
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
•	Prototype: def class_to_json(obj):
•	obj is an instance of a Class
•	All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean
•	Not allowed to import any module
No test cases needed

9. Student to JSON
Write a class Student that defines a student by:
•	Public instance attributes:
o	first_name
o	last_name
o	age
•	Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
•	Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
•	Not allowed to import any module
No test cases needed

10. Student to JSON with filter
Write a class Student that defines a student by: (based on 9-student.py)
•	Public instance attributes:
o	first_name
o	last_name
o	age
•	Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
•	Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
o	If attrs is a list of strings, only attribute names contained in this list must be retrieved.
o	Otherwise, all attributes must be retrieved
•	Not allowed to import any module
No test cases needed


11. Student to disk and reload
Write a class Student that defines a student by: (based on 10-student.py)
•	Public instance attributes:
o	first_name
o	last_name
o	age
•	Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
•	Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
o	If attrs is a list of strings, only attributes name contain in this list must be retrieved.
o	Otherwise, all attributes must be retrieved
•	Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
o	You can assume json will always be a dictionary
o	A dictionary key will be the public attribute name
o	A dictionary value will be the value of the public attribute
•	Not allowed to import any module
Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)

12. Pascal's Triangle
Technical interview preparation:
•	Not allowed to google anything
•	Whiteboard first
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:
•	Returns an empty list if n <= 0
•	You can assume n will be always an integer
•	Not allowed to import any module

13. Search and update
Write a function that inserts a line of text to a file, after each line containing a specific string (see example):
•	Prototype: def append_after(filename="", search_string="", new_string=""):
•	You must use the with statement
•	No need to manage file permission or file doesn't exist exceptions.
•	Not allowed to import any module
No test cases needed

14. Log parsing
Write a script that reads stdin line by line and computes metrics:
•	Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
•	Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
o	Total file size: File size: <total size>
o	where is the sum of all previous (see input format above)
o	Number of lines by status code:
	possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
	if a status code doesn’t appear, don’t print anything for this status code
	format: <status code>: <number>
	status codes should be printed in ascending order
No test cases needed
