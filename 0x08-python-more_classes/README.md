0x08. Python - More Classes and Objects

Learning Objectives
In this project I have learnt :
•	Why Python programming is awesome
•	What OOP is 
•	“first-class everything”
•	What a class is
•	What an object and an instance is
•	The difference between a class and an object or instance
•	What an attribute is
•	What are and how to use public, protected and private attributes
•	What self is
•	What a method is
•	What is the special __init__ method and how to use it
•	What is Data Abstraction, Data Encapsulation, and Information Hiding
•	What a property is
•	The difference between an attribute and a property in Python
•	The Pythonic way to write getters and setters in Python
•	The special __str__ and __repr__ methods and how to use them
•	The difference between __str__ and __repr__
•	What a class attribute is
•	The difference between a object attribute and a class attribute
•	What a class method is
•	What a static method is
•	How to dynamically create arbitrary new attributes for existing instances of a class
•	How to bind attributes to object and classes
•	What is and what does contain __dict__ of a class and of an instance of a class
•	How does Python find the attributes of an object or class
•	How to use the getattr function

Tasks
0. Simple rectangle
Write an empty class Rectangle that defines a rectangle:
•	Not allowed to import any module

1. Real definition of a rectangle
Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
•	Private instance attribute: width:
o	property def width(self): to retrieve it
o	property setter def width(self, value): to set it:
	width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
	if width is less than 0, raise a ValueError exception with the message width must be >= 0
•	Private instance attribute: height:
o	property def height(self): to retrieve it
o	property setter def height(self, value): to set it:
	height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
	if height is less than 0, raise a ValueError exception with the message height must be >= 0
•	Instantiation with optional width and height: def __init__(self, width=0, height=0):
•	Not allowed to import any module
2. Area and Perimeter
Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
•	Private instance attribute: width:
o	property def width(self): to retrieve it
o	property setter def width(self, value): to set it:
	width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
	if width is less than 0, raise a ValueError exception with the message width must be >= 0
•	Private instance attribute: height:
o	property def height(self): to retrieve it
o	property setter def height(self, value): to set it:
	height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
	if height is less than 0, raise a ValueError exception with the message height must be >= 0
•	Instantiation with optional width and height: def __init__(self, width=0, height=0):
•	Public instance method: def area(self): that returns the rectangle area
•	Public instance method: def perimeter(self): that returns the rectangle perimeter:
o	if width or height is equal to 0, perimeter is equal to 0
•	Not allowed to import any module

3. String representation
Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
•	Private instance attribute: width:
o	property def width(self): to retrieve it
o	property setter def width(self, value): to set it:
	width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
	if width is less than 0, raise a ValueError exception with the message width must be >= 0
•	Private instance attribute: height:
o	property def height(self): to retrieve it
o	property setter def height(self, value): to set it:
	height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
	if height is less than 0, raise a ValueError exception with the message height must be >= 0
•	Instantiation with optional width and height: def __init__(self, width=0, height=0):
•	Public instance method: def area(self): that returns the rectangle area
•	Public instance method: def perimeter(self): that returns the rectangle perimeter:
o	if width or height is equal to 0, perimeter has to be equal to 0
•	print() and str() should print the rectangle with the character #: (see example below)
o	if width or height is equal to 0, return an empty string
•	Not allowed to import any module

4. Eval is magic
Write a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)
•	Private instance attribute: width:
o	property def width(self): to retrieve it
o	property setter def width(self, value): to set it:
	width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
	if width is less than 0, raise a ValueError exception with the message width must be >= 0
•	Private instance attribute: height:
o	property def height(self): to retrieve it
o	property setter def height(self, value): to set it:
	height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
	if height is less than 0, raise a ValueError exception with the message height must be >= 0
•	Instantiation with optional width and height: def __init__(self, width=0, height=0):
•	Public instance method: def area(self): that returns the rectangle area
•	Public instance method: def perimeter(self): that returns the rectangle perimeter:
o	if width or height is equal to 0, perimeter has to be equal to 0
•	print() and str() should print the rectangle with the character #: (see example below)
o	if width or height is equal to 0, return an empty string
•	repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() (see example below)
•	Not allowed to import any module


5. Detect instance deletion
Write a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)
•	Private instance attribute: width:
o	property def width(self): to retrieve it
o	property setter def width(self, value): to set it:
	width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
	if width is less than 0, raise a ValueError exception with the message width must be >= 0
•	Private instance attribute: height:
o	property def height(self): to retrieve it
o	property setter def height(self, value): to set it:
	height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
	if height is less than 0, raise a ValueError exception with the message height must be >= 0
•	Instantiation with optional width and height: def __init__(self, width=0, height=0):
•	Public instance method: def area(self): that returns the rectangle area
•	Public instance method: def perimeter(self): that returns the rectangle perimeter:
o	if width or height is equal to 0, perimeter has to be equal to 0
•	print() and str() should print the rectangle with the character #:
o	if width or height is equal to 0, return an empty string
•	repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
•	Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
•	Not allowed to import any module


6. How many instances
Write a class Rectangle that defines a rectangle by: (based on 5-rectangle.py)
•	Private instance attribute: width:
o	property def width(self): to retrieve it
o	property setter def width(self, value): to set it:
	width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
	if width is less than 0, raise a ValueError exception with the message width must be >= 0
•	Private instance attribute: height:
o	property def height(self): to retrieve it
o	property setter def height(self, value): to set it:
	height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
	if height is less than 0, raise a ValueError exception with the message height must be >= 0
•	Public class attribute number_of_instances:
o	Initialized to 0
o	Incremented during each new instance instantiation
o	Decremented during each instance deletion
•	Instantiation with optional width and height: def __init__(self, width=0, height=0):
•	Public instance method: def area(self): that returns the rectangle area
•	Public instance method: def perimeter(self): that returns the rectangle perimeter:
o	if width or height is equal to 0, perimeter has to be equal to 0
•	print() and str() should print the rectangle with the character #:
o	if width or height is equal to 0, return an empty string
•	repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
•	Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
•	Not allowed to import any module

7. Change representation
Write a class Rectangle that defines a rectangle by: (based on 6-rectangle.py)
•	Private instance attribute: width:
o	property def width(self): to retrieve it
o	property setter def width(self, value): to set it:
	width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
	if width is less than 0, raise a ValueError exception with the message width must be >= 0
•	Private instance attribute: height:
o	property def height(self): to retrieve it
o	property setter def height(self, value): to set it:
	height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
	if height is less than 0, raise a ValueError exception with the message height must be >= 0
•	Public class attribute number_of_instances:
o	Initialized to 0
o	Incremented during each new instance instantiation
o	Decremented during each instance deletion
•	Public class attribute print_symbol:
o	Initialized to #
o	Used as symbol for string representation
o	Can be any type
•	Instantiation with optional width and height: def __init__(self, width=0, height=0):
•	Public instance method: def area(self): that returns the rectangle area
•	Public instance method: def perimeter(self): that returns the rectangle perimeter:
o	if width or height is equal to 0, perimeter has to be equal to 0
•	print() and str() should print the rectangle with the character(s) stored in print_symbol:
o	if width or height is equal to 0, return an empty string
•	repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
•	Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
•	Not allowed to import any module


8. Compare rectangles
Write a class Rectangle that defines a rectangle by: (based on 7-rectangle.py)
•	Private instance attribute: width:
o	property def width(self): to retrieve it
o	property setter def width(self, value): to set it:
	width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
	if width is less than 0, raise a ValueError exception with the message width must be >= 0
•	Private instance attribute: height:
o	property def height(self): to retrieve it
o	property setter def height(self, value): to set it:
	height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
	if height is less than 0, raise a ValueError exception with the message height must be >= 0
•	Public class attribute number_of_instances:
o	Initialized to 0
o	Incremented during each new instance instantiation
o	Decremented during each instance deletion
•	Public class attribute print_symbol:
o	Initialized to #
o	Used as symbol for string representation
o	Can be any type
•	Instantiation with optional width and height: def __init__(self, width=0, height=0):
•	Public instance method: def area(self): that returns the rectangle area
•	Public instance method: def perimeter(self): that returns the rectangle perimeter:
o	if width or height is equal to 0, perimeter has to be equal to 0
•	print() and str() should print the rectangle with the character #:
o	if width or height is equal to 0, return an empty string
•	repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
•	Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
•	Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area
o	rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle
o	rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle
o	Returns rect_1 if both have the same area value
•	Not allowed to import any module
9. A square is a rectangle
Write a class Rectangle that defines a rectangle by: (based on 8-rectangle.py)
•	Private instance attribute: width:
o	property def width(self): to retrieve it
o	property setter def width(self, value): to set it:
	width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
	if width is less than 0, raise a ValueError exception with the message width must be >= 0
•	Private instance attribute: height:
o	property def height(self): to retrieve it
o	property setter def height(self, value): to set it:
	height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
	if height is less than 0, raise a ValueError exception with the message height must be >= 0
•	Public class attribute number_of_instances:
o	Initialized to 0
o	Incremented during each new instance instantiation
o	Decremented during each instance deletion
•	Public class attribute print_symbol:
o	Initialized to #
o	Used as symbol for string representation
o	Can be any type
•	Instantiation with optional width and height: def __init__(self, width=0, height=0):
•	Public instance method: def area(self): that returns the rectangle area
•	Public instance method: def perimeter(self): that returns the rectangle perimeter:
o	if width or height is equal to 0, perimeter has to be equal to 0
•	print() and str() should print the rectangle with the character #:
o	if width or height is equal to 0, return an empty string
•	repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
•	Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
•	Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area
o	rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle
o	rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle
o	Returns rect_1 if both have the same area value
•	Class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size
•	Not allowed to import any module

10. N queens
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.
•	Usage: nqueens N
o	If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
•	where N must be an integer greater or equal to 4
o	If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
o	If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
•	The program should print every possible solution to the problem
o	One solution per line
o	Format: see example
o	You don’t have to print the solutions in a specific order
•	only allowed to import the sys module
