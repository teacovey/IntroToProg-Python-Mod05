# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# New concepts: the use of data processing using dictionaries and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   thcov,6/03/2026,Created script from starter
# ------------------------------------------------------------------------------------------ #
import json
# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"
# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
file = None  # Holds a reference to an opened file.
menu_choice: str = ''  # Hold the choice made by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
except FileNotFoundError as e:
    print("This file doesn't exist.")
    print("---Technical Information---")
    print(e, e.__doc__,type(e),sep='\n')
    print("Creating a new file...")
    file=open(FILE_NAME, "w")
except JSONDecodeError as e:
    print("File data is invalid.")
    print("---Technical Information---")
    print(e, e.__doc__, type(e), sep='\n')
    print('Resetting file data...')
    file = open(FILE_NAME, "w")
    json.dump(student_data, file)
except Exception as e:
    print("There was an error opening the file.")
    print("---Technical Information---")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if not file.closed:
        file.close()

# Present and Process the data
while (True):
    # Present the menu of choices
    print(MENU)
    menu_choice = input("Please make a selection: ")
    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("First name can only contain alphabetic characters.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Last name can only contain alphabetic characters.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName":student_first_name,"LastName":student_last_name,"CourseName":course_name}
            students.append(student_data)
            print(f"{student_first_name} {student_last_name} is now registered for {course_name}.")
        except ValueError as e:
            print(e)
            print("Invalid entry. Please try again...")
            print("---Technical Information---")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("There was an issue with your entry.")
            print("---Technical Information---")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        for student_data in students:
            student_first_name = student_data["FirstName"]
            student_last_name = student_data["LastName"]
            course_name = student_data["CourseName"]
            print(f"{student_first_name},{student_last_name},{course_name}")
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=2)
            print("The following data was saved to " + FILE_NAME)
            for student in students:
                print(f'{student["FirstName"]} {student["LastName"]} is registered for {student["CourseName"]}')
        except TypeError as e:
            print("JSON data was malformed.")
            print("---Technical Information---")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("There was an error saving data to the file.")
            print("---Technical Information---")
            print(e, e.__doc__, type(e), sep='\n')
        # Check if a file object exists and is still open
        finally:
            if not file.closed:
                file.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Invalid selection. Please enter 1, 2, 3, or 4.")

print("Program Ended")
