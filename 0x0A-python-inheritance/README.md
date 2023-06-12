0x0A. Python - Inheritance
Python OOP Inheritance
In this Module I have learnt the following:
•	superclass, baseclass or parentclass
•	What a subclass is
•	How to list all attributes and methods of a class or instance
•	When can an instance have new attributes
•	How to inherit class from another
•	How to define a class with multiple base classes
•	The default class every class inherit from
•	How to override a method or attribute inherited from the base class
•	Which attributes or methods are available by heritage to subclasses
•	The purpose of inheritance
•	What are, when and how to use isinstance, issubclass, type and super built-in functions
Documentation
•	Do not use the words import or from inside your comments, the checker will think you try to import some modules
Tasks
0. Lookup
Write a function that returns the list of available attributes and methods of an object:
•	Prototype: def lookup(obj):
•	Returns a list object
•	Not allowed to import any module
No test cases needed


1. My list
Write a class MyList that inherits from list:
•	Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
•	Assumes that all the elements of the list will be of type int
•	Not allowed to import any module
2. Exact same object
Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
•	Prototype: def is_same_class(obj, a_class):
•	Not allowed to import any module
No test cases needed



3. Same class or inherit from
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
•	Prototype: def is_kind_of_class(obj, a_class):
•	You are not allowed to import any module
No test cases needed



4. Only sub class of
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
•	Prototype: def inherits_from(obj, a_class):
•	Not allowed to import any module
No test cases needed



5. Geometry module
Write an empty class BaseGeometry.
•	Not allowed to import any module
Repo:
•	GitHub repository: alx-higher_level_programming
•	Directory: 0x0A-python-inheritance
•	File: 5-base_geometry.py

6. Improve Geometry
Write a class BaseGeometry (based on 5-base_geometry.py).
•	Public instance method: def area(self): that raises an Exception with the message area() is not implemented
•	Not allowed to import any module
No test cases needed


7. Integer validator
Write a class BaseGeometry (based on 6-base_geometry.py).
•	Public instance method: def area(self): that raises an Exception with the message area() is not implemented
•	Public instance method: def integer_validator(self, name, value): that validates value:
o	you can assume name is always a string
o	if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
o	if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
•	Not allowed to import any module



8. Rectangle
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
•	Instantiation with width and height: def __init__(self, width, height):
o	width and height must be private. No getter or setter
o	width and height must be positive integers, validated by integer_validator
No test cases needed
Repo:
•	GitHub repository: alx-higher_level_programming
•	Directory: 0x0A-python-inheritance
•	File: 8-rectangle.py





9. Full rectangle
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)
•	Instantiation with width and height: def __init__(self, width, height)::
o	width and height must be private. No getter or setter
o	width and height must be positive integers validated by integer_validator
•	the area() method must be implemented
•	print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>
No test cases needed



10. Square #1
Write a class Square that inherits from Rectangle (9-rectangle.py):
•	Instantiation with size: def __init__(self, size)::
o	size must be private. No getter or setter
o	size must be a positive integer, validated by integer_validator
•	the area() method must be implemented
No test cases needed


11. Square #2
Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).
•	Instantiation with size: def __init__(self, size)::
o	size must be private. No getter or setter
o	size must be a positive integer, validated by integer_validator
•	the area() method must be implemented
•	print() should print, and str() should return, the square description: [Square] <width>/<height>
No test cases needed



12. My integer
Write a class MyInt that inherits from int:
•	MyInt is a rebel. MyInt has == and != operators inverted
•	Not allowed to import any module
No test cases needed




13. Can I?
Write a function that adds a new attribute to an object if it’s possible:
•	Raise a TypeError exception, with the message can't add new attribute if the object can’t have new attribute
•	You are not allowed to use try/except
•	Not allowed to import any module

