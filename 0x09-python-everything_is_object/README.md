0x09. Python - Everything is object
Learning Objectives
In this project I have learnt the below lessons
•	What an object is
•	The difference between a class and an object or instance
•	The difference between immutable object and mutable object
•	What a reference is
•	What an assignment is
•	What an alias is
•	How to know if two variables are identical
•	How to know if two variables are linked to the same object
•	How to display the variable identifier (which is the memory address in the CPython implementation)
•	What mutable and immutable is
•	What are the built-in mutable types
•	The built-in immutable types
•	How Python pass variables to functions
Python Scripts
•	All files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
•	All files ends with a newline character
•	The first line of all script files are exactly #!/usr/bin/python3
•	A README.md file, at the root of the folder of the project, is mandatory
•	code uses the pycodestyle (version 2.8.*)
•	All your files are executable
•	The length of all comply with wc tested
.txt Answer Files
•	Only one line
•	No Shebang
•	All files ends with a new line
Tasks
0.	Who am I?
This function would is used to get the type of an object?
Writing the name of the function in the file, without ().


1. Where are you?
How to get the variable identifier (which is the memory address in the CPython implementation)?
Writing the name of the function in the file, without ().


2. Right count
In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = 100


3. Right count =
In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = 89


4. Right count =
In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = a


5. Right count =+
In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = a + 1





6. Is equal
What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)


7. Is the same
What do these 3 lines print?
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)



8. Is really equal
What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)


9. Is really the same
What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)


10. And with a list, is it equal
What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
11. And with a list, is it the same
What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)


12. And with a list, is it really equal
What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)


13. And with a list, is it really the same
What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
 

14. List append
What does this script print?
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
 

15. List add
What does this script print?
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)


16. Integer incrementation
What does this script print?
def increment(n):
    n += 1

a = 1
increment(a)
print(a)



17. List incrementation
The result for below script print?
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)


18. List assignation
What does this script print?
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)


19. Copy a list object
This function def copy_list(l): that returns a copy of a list.
•	The input list can contain any type of objects
•	files have maximum 3-line long (no documentation needed)
•	Not allowed to import any module

20. Tuple or not?
a = ()
Is a a tuple? Answer with Yes or No.


21. Tuple or not?
a = (1, 2)
Is a a tuple? Answer with Yes or No.


22. Tuple or not?
a = (1)
Is a a tuple? Answer with Yes or No.



23. Tuple or not?
a = (1, )
Is a a tuple? Answer with Yes or No.


24. Who I am?

What does this script print?
a = (1)
b = (1)
a is b

25. Tuple or not
What does this script print?
a = (1, 2)
b = (1, 2)
a is b
26. Empty is not empty
What the below script print?
a = ()
b = ()
a is b


27. Still the same?
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.


28. Same or not?
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.


29. #pythonic
Write a function magic_string() that returns a string “BestSchool” n times the number of the iteration (see code):
•	Format: see example
•	file has maximum 4-line long (no documentation needed)
•	Not allowed to import any module
30. Low memory cost
a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.
•	You are not allowed to import any module
31. int 1/3
Assuming we are using a CPython implementation of Python3 with default options/configuration:
•	How many int objects are created by the execution of the first line of the script? (103-line1.txt)
•	How many int objects are created by the execution of the second line of the script (103-32. int 2/3
Assuming we are using a CPython implementation of Python3 with default options/configuration:
•	How many int objects are created by the execution of the first line of the script? (104-line1.txt)
•	How many int objects are created by the execution of the second line of the script (104-line2.txt)
•	After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (104-line3.txt)
•	After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (104-line4.txt)
•	How many int objects are created by the execution of the last line of the script (104-line5.txt)

33. int 3/3
Assuming we are using a CPython implementation of Python3 with default options/configuration:
•	Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory? (105-line1.txt)
•	Why? (optional blog post :))
Hint: NSMALLPOSINTS, NSMALLNEGINTS

34. Clear strings
Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):
•	How many string objects are created by the execution of the first line of the script? (106-line1.txt)
•	How many string objects are created by the execution of the second line of the script (106-line2.txt)
•	After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)
•	After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)
•	How many string objects are created by the execution of the last line of the script (106-line5.txt)

