import mysql.connector as mysql
import os,sys
from time import sleep

database = mysql.connect(host="localhost",user="root",password="",database="school_sys")
mysql = database.cursor()


def admin_session():
	while 1:
		os.system("clear")
		print("""
+------------------+
|Logged in as Admin|
+------------------+

1. Add new teacher
2. Add new student
3. Delete teacher
4. Delete student
5. Logout
""")
		print("ID Name Pass:")
		mysql.execute("SELECT id,username,privilege FROM user")
		users = mysql.fetchall()
		for user in users:
			user = str(user).replace("'","")
			user = str(user).replace(",","")
			user = str(user).replace("(","")
			user = str(user).replace(")","")
			print(user + "\n")
		choice = input(str("Option: "))

		if choice == "1":
  		  print("Add new teacher")
  		  print("")
  		  username = input(str("Teacher username: "))
  		  password = input(str("Teacher password: "))
  		  mysql.execute("INSERT INTO user (username,password,privilege) VALUES (%s,%s,'teacher')", (username,password))
  		  print(username + " has been added as a teacher")
  		    		  	  
		elif choice == "2":
			print("Add new student")
			print("")
			username = input(str("Student username: "))
			password = input(str("Student password: "))
			mysql.execute("INSERT INTO user (username,password,privilege) VALUES (%s,%s,'student')", (username,password))
			print(username + " has been added as a student")
			
		elif choice == "3":
			print("Delete a teacher")
			print("")
			print("Teacher's Account")
			print("")
			username = input(str("Teacher name: "))
			mysql.execute("DELETE FROM user WHERE username = %s AND privilege = %s", (username,"teacher"))
			if mysql.fetchone() is not None:
				print("User " + username + " have been deleted")
			else:
				print("Theres no user " + username + " in the database")
				
		elif choice == "4":
			print("Delete a student")
			print("")
			username = input(str("Student name: "))
			mysql.execute("DELETE FROM user WHERE username = %s AND privilege = %s", (username,"student"))
			if mysql.fetchone() is not None:
				print("User " + username + " have been deleted")
			else:
				print("Theres no user " + username + " in the database")

		elif choice == "5":
			os.system("clear")
			break
						
		else:
		    print("Error please try again") 

def admin_auth():
	os.system("clear")
	print("""
+--------------+
|Login as Admin|
+--------------+
""")
	username = input(str("Username: "))
	password = input(str("Password: "))
	if username == "admin":
			if password == "admin":
					admin_session()
	else:
			print("Wrong username or password")


def teacher_session():
	while 1:
		os.system("clear")
		print("""
+--------------------+
|Logged in as Teacher|
+--------------------+

Option:
1. Class Record
2. Add Quiz
3. Logout
""")
		print("")
		choice = input(str("Option: "))
		
		if choice == "1":
			print("This is class record")		
		elif choice == "2":
			print("This is add quiz")
		elif choice == "3":
			os.system("clear")
			break
		else:
			print("error")
		

def teacher_auth():
	os.system("clear")
	print("""
+----------------+
|Login as Teacher|
+----------------+
""")
	username = input(str("Username: "))
	password = input(str("Password: "))
	mysql.execute("SELECT * FROM user WHERE username = %s AND password = %s AND privilege='teacher'", (username,password))
	if mysql.fetchone() is not None:
		teacher_session()
	else:
		print("error")


def student_session():
	while 1:
		os.system("clear")
		print("""
+------------------+
|Logged in as Student|
+------------------+

Option:
1. Quiz Score
2. Take Quiz
3. Logout
""")
		choice = input(str("Option: "))
		
		if choice == "1":
			print("This is quiz score")
		elif choice == "2":
			print("This is take quiz")
		elif choice == "3":
			os.system("clear")
			break
		else:
			print("error")
		
def student_auth():
	os.system("clear")
	print("""
+----------------+
|Login as Student|
+----------------+
""")
	username = input(str("Username: "))
	password = input(str("Password: "))
	mysql.execute("SELECT * FROM user WHERE username = %s AND password = %s AND privilege='student'", (username,password))
	if mysql.fetchone() is not None:
		student_session()
	else:
		print("error")

def main():
	while 1:
		print("""
	Welcome to school management system
		
Option:
1. Admin
2. Teacher
3. Student
4. Exit
		""")		
		choice = input(str("Login as: "))
		
		if choice == "1":
			admin_auth()			
		elif choice == "2":
			teacher_auth()
		elif choice == "3":
			student_auth()
		elif choice == "4":
			exit()
		else:
			print("Invalid option. Please try again")			
main()