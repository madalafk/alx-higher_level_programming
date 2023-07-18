0x0D. SQL - Introduction
SQL    | MySQL

Learning Objectives
In this project I have learnt the below things :
•	What’s a database
•	What’s a relational database
•	What does SQL stand for
•	What’s MySQL
•	How to create a database in MySQL
•	What does DDL and DML stand for
•	How to CREATE or ALTER a table
•	How to SELECT data from a table
•	How to INSERT, UPDATE or DELETE data
•	What are subqueries
•	How to use MySQL functions

Tasks
0. List databases
a script that lists all databases of your MySQL server.

1. Create a database
a script that creates the database hbtn_0c_0 in your MySQL server.
•	If the database hbtn_0c_0 already exists, your script should not fail
•	You are not allowed to use the SELECT or SHOW statements
2. Delete a database
a script that deletes the database hbtn_0c_0 in your MySQL server.
•	If the database hbtn_0c_0 doesn’t exist, your script should not fail
•	You are not allowed to use the SELECT or SHOW statements
3. List tables
a script that lists all the tables of a database in your MySQL server.
•	The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)
4. First table
a script that creates a table called first_table in the current database in your MySQL server.
•	first_table description:
o	id INT
o	name VARCHAR(256)
•	The database name will be passed as an argument of the mysql command
•	If the table first_table already exists, your script should not fail
•	Not allowed to use the SELECT or SHOW statements
5. Full description
a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
•	The database name will be passed as an argument of the mysql command
•	Not allowed to use the DESCRIBE or EXPLAIN statements

6. List all in table
a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
•	All fields are be printed
•	The database name will be passed as an argument of the mysql command

7. First add
a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.
•	New row:
o	id = 89
o	name = Best School
•	The database name will be passed as an argument of the mysql command

8. Count 89
a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
•	The database name will be passed as an argument of the mysql command

9. Full creation
a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
•	second_table description:
o	id INT
o	name VARCHAR(256)
o	score INT
•	The database name will be passed as an argument to the mysql command
•	If the table second_table already exists, this script should not fail
•	Not allowed to use the SELECT and SHOW statements
•	This script creates these records:
o	id = 1, name = “John”, score = 10
o	id = 2, name = “Alex”, score = 3
o	id = 3, name = “Bob”, score = 14
o	id = 4, name = “George”, score = 8

10. List by best
a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
•	Results should display both the score and the name (in this order)
•	Records should be ordered by score (top first)
•	The database name will be passed as an argument of the mysql command




