0x05. Python - Exceptions

Learning Objectives
I have learnt the following:
•	Why Python programming is awesome
•	The difference between errors and exceptions
•	Eexceptions and how they are used
•	When do we need to use exceptions
•	How to correctly handle an exception
•	The purpose of catching exceptions
•	How to raise a builtin exception
•	When do we need to implement a clean-up action after an exception

Tasks
0. Safe list printing
This function prints x elements of a list.
•	Prototype: def safe_print_list(my_list=[], x=0):
•	my_list can contain any type (integer, string, etc.)
•	All elements must be printed on the same line followed by a new line.
•	x represents the number of elements to print
•	x can be bigger than the length of my_list
•	Returns the real number of elements printed
•	Used try: / except:
•	not allowed to import any module
•	not allowed to use len()

1. Safe printing of an integers list
This function prints an integer with "{:d}".format().
•	Prototype: def safe_print_integer(value):
•	value can be any type (integer, string, etc.)
•	The integer should be printed followed by a new line
•	Returns True if value has been correctly printed (it means the value is an integer)
•	Otherwise, returns False
•	Used try: / except:
•	Used "{:d}".format() to print as integer
•	Not allowed to import any module
•	Not allowed to use type()

2. Print and count integers
This function prints the first x elements of a list and only integers.
•	Prototype: def safe_print_list_integers(my_list=[], x=0):
•	my_list can contain any type (integer, string, etc.)
•	All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
•	x represents the number of elements to access in my_list
•	x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur
•	Returns the real number of integers printed
•	Used try: / except:
•	Used "{:d}".format() to print an integer
•	not allowed to import any module
•	not allowed to use len()

3. Integers division with debug
This  function divides 2 integers and prints the result.
•	Prototype: def safe_print_division(a, b):
•	You can assume that a and b are integers
•	The result of the division should print on the finally: section preceded by Inside result:
•	Returns the value of the division, otherwise: None
•	Used try: / except: / finally:
•	Used "{}".format() to print the result
•	not allowed to import any module

4. Divide a list
This function divides element by element 2 lists.
•	Prototype: def list_division(my_list_1, my_list_2, list_length):
•	my_list_1 and my_list_2 can contain any type (integer, string, etc.)
•	list_length can be bigger than the length of both lists
•	Returns a new list (length = list_length) with all divisions
•	If 2 elements can’t be divided, the division result should be equal to 0
•	If an element is not an integer or float:
o	print: wrong type
•	If the division can’t be done (/0):
o	print: division by 0
•	If my_list_1 or my_list_2 is too short
o	print: out of range
•	Used try: / except: / finally:
•	not allowed to import any module

5. Raise exception
Write a function that raises a type exception.
•	Prototype: def raise_exception():
•	allowed to import any module

6. Raise a message
This  function raises a name exception with a message.
•	Prototype: def raise_exception_msg(message=""):
•	You are not allowed to import any module
7. Safe integer print with error message
This function prints an integer.
•	Prototype: def safe_print_integer_err(value):
•	value can be any type (integer, string, etc.)
•	The integer should be printed followed by a new line
•	Returns True if value has been correctly printed (it means the value is an integer)
•	Otherwise, returns False and prints in stderr the error precede by Exception:
•	Used try: / except:
•	Used "{:d}".format() to print as integer
•	not allowed to use type()

8. Safe function
This function executes a function safely.
•	Prototype: def safe_function(fct, *args):
•	You can assume fct will be always a pointer to a function
•	Returns the result of the function,
•	Otherwise, returns None if something happens during the function and prints in stderr the error precede by Exception:
•	You have to use try: / except:

9. ByteCode -> Python #4
This Python function def magic_calculation(a, b): 

10. CPython #2: PyFloatObject
Create three C functions that print some basic info about Python lists, Python bytes an Python float objects.

Python lists:
•	Prototype: void print_python_list(PyObject *p);
•	Format: see example
•	If p is not a valid PyListObject, print an error message (see example)
Python bytes:
•	Prototype: void print_python_bytes(PyObject *p);
•	Format: see example
•	Line “first X bytes”: print a maximum of 10 bytes
•	If p is not a valid PyBytesObject, print an error message (see example)
Python float:
•	Prototype: void print_python_float(PyObject *p);
•	Format: see example
•	If p is not a valid PyFloatObject, print an error message (see example)
•	Read /usr/include/python3.4/floatobject.h
About:
•	Python version: 3.4
•	Allowed to use the C standard library
•	shared library compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
•	not allowed to use the following macros/functions:
o	Py_SIZE
o	Py_TYPE
o	PyList_Size
o	PyList_GetItem
o	PyBytes_AS_STRING
o	PyBytes_GET_SIZE
o	PyBytes_AsString
o	PyBytes_AsStringAndSize
o	PyFloat_AS_DOUBLE
o	PySequence_GetItem
o	PySequence_Fast_GET_SIZE
o	PySequence_Fast_GET_ITEM
o	PySequence_ITEM
o	PySequence_Fast_ITEMS
NOTE:
•	The python script will be launched using the -u option (Force stdout to be unbuffered).
•	strongly advised to either use setbuf(stdout, NULL); or fflush(stdout) in your C functions IF you choose to use printf. The reason to that is that Pythonsprintand libCs printf don’t share the same buffer, and the output can appear disordered.

