ALX 0x02. Python - import & modules

Lessons learnt in this project
>>> Why Python programming is awesome
>>> How to import functions from another file
>>> How to use imported functions
>>> How to create a module
>>> How to use the built-in function dir()
>>> How to prevent code in the script from being executed when imported
>>> How to use command line arguments with your Python programs

TASKS.
>>> 0. Import a simple function from a simple file
	A program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3

	use print function with string format to display integers

	assign:   the value 1 to a variable called a
              the value 2 to a variable called b
              use those two variables as arguments when calling the functions add and print
              a and b must be defined in 2 different lines: a = 1 and another b = 2
	program prints : <a value> + <b value> = <add(a, b) value> followed with a new line
             word add_0 once in used only once in the code
	(* for importing or __import__ ) not allowed 
	code should not be executed when imported - by using __import


>>> 1. My first toolbox!
	Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.
	function print used (with string format to display integers) more than 4 times

	defined:
           the value 10 to a variable a
           the value 5 to a variable b
           use these two variables only, as arguments when calling functions (including print)
           a and b must be defined in 2 different lines: a = 10 and another b = 5
	program calls each of the imported functions.

>>> 2. How to make a script dynamic!
	This program prints the number of and the list of its arguments.
        The output is:
         Number of argument(s) followed by argument (if number is one) or arguments
	 (otherwise), followed by : (or. if no arguments were passed) followed by a new line, 
	 followed by (if at least one argument), one line per argument: the position of the a
	 rgument (starting at 1) followed by :, followed by the argument value and a new line
	code is not executed when imported
	The number of elements of argv can be retrieved by using: len(argv)
   
>>> 3. Infinite addition
	This program prints the result of the addition of all arguments
	output is the result of the addition of all arguments, followed by a new line
	arguments are cast into integers by using int() (assuming that all arguments can be casted into integers)
	code is not executed when imported
	program also handles big numbers.    
>>> 4. Who are you?
	This program prints all the names defined by the compiled module hidden_4.pyc
	Printed  one name per line, in alpha order
	prints only names that do not start with __
	code is not be executed when imported   
>>> 5. Everything can be imported
	This program imports the variable a from the file variable_load_5.py and prints its value.
	(* for importing or __import__) not used 
	code is not executed when imported
>>> 6. Build my own calculator!
This program imports all functions from the file calculator_1.py and handles basic operations.
	Usage: ./100-my_calculator.py a operator b
	If the number of arguments is not 3, your program has to:
	print Usage: ./100-my_calculator.py <a> <operator> <b> followed with a new line
	exit with the value 1
	operator are:
           + for addition
           - for subtraction
           * for multiplication
           / for division
	If the operator is not one of the above:
            print Unknown operator. Available operators: +, -, * and / followed with a new line
            exit with the value 1
	cast a and b into integers by using int() (you can assume that all arguments will be castable into integers)
	The printed like this: <a> <operator> <b> = <result>, followed by a new line
	code is not executed when imported

   
>>> 7. Easy print
	This program prints #pythoniscool, followed by a new line, in the standard output.
	program has a maximum of 2 lines long
	print or eval or open or import sys not used in the  file 101-easy_print.py 
   
>>> 8. ByteCode -> Python #3
	Python function def magic_calculation(a, b): 
   
>>> 9. Fast alphabet
	This program that prints the alphabet in uppercase, followed by a new line.
	program as a maximum of 3 lines long
	not used: 
any loops
           any conditional statements
           str.join()
           any string literal
           any system calls
