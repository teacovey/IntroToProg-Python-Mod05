# ------------------------------------------------------------------------------------------ #
# Title: Working With Exceptions/Working With JSON Files/Working With Dictionaries And Files
# Desc: Shows how to work with exceptions/Shows how to work with JSON files/Shows how work with dictionaries and files when using a table of data
# Change Log: (Who, When, What)
# thcov,5/20/2026,Created Script
# thcov,5/20/2026,Copied all code from Mod05-Lab02 to this script
# thcov,5/20/2026,Made updates to script according to instructions for Mod05-Lab03
# Notes: This is built off the Mod05-Lab02 script (and Mod05-Lab02 built off the script from Mod05-Lab01).
# ------------------------------------------------------------------------------------------ #
import json
# Define the Data Constants
FILE_NAME: str = 'MyLabData.json'

# Define the program's data
MENU: str= '''
---- Student GPAs -----------------------
Select from the following menu:
    1. Show current student data.
    2. Enter new student data.
    3. Save data to a file.
    4. Exit the program.
-----------------------------------------
'''
student_first_name: str=''
student_last_name: str=''
student_gpa: float= 0.0
message: str=''
menu_choice: str=''
student_data: dict={}
students: list=[]
file_data:str=''
file=None
# When the program starts, read the file data into a list of dictionary rows (table)
# Extract the data from the file

# file=open(FILE_NAME, "r")
# for row in file.readlines():
#     # Transform the data from the file
#     student_data=row.split(',')
#     student_data={"FirstName":student_data[0],
#                   "LastName": student_data[1],
#                   "GPA": float(student_data[2].strip())}
    # Load it into the collection
#     students.append(student_data)
# file.close()
try:
    file=open(FILE_NAME, "r")
    students = json.load(file)

except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("--Technical Error Message--")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("--Technical Error Message--")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file is not None and file.close ==False:
        file.close()

# Repeat the follow tasks
while True:
# display the table's current data
    print(MENU)
    menu_choice=input("Enter your menu choice number: ")
    print()
    if menu_choice=='1':
        print("-" * 50)
        for student in students:
            if student["GPA"] >= 4.0:
                message = " {} {} earned an A with a {:.2f} GPA"
            elif student["GPA"] >= 3.0:
                message = " {} {} earned a B with a {:.2f} GPA"
            elif student["GPA"] >= 2.0:
                message = " {} {} earned a C with a {:.2f} GPA"
            elif student["GPA"] >= 1.0:
                message = " {} {} earned a D with a {:.2f} GPA"
            else:
                message = " {} {}'s {:.2f} GPA was not a passing grade"
            print(message.format(student["FirstName"], student["LastName"], student["GPA"]))
        print("-" * 50)
    elif menu_choice == '2':
        try:
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            try: # using a nested try block to capture when an input cannot be changed to a float
                student_gpa = float(input("What is the student's GPA? "))
            except ValueError:
                raise ValueError("GPA must be a numeric value.")

            student_data = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "GPA": student_gpa}
            students.append(student_data)
        except ValueError as e:
            print(e) #Prints the custom message
            print("--Technical Error Message--")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("--Technical Error Message--")
            print(e, e.__doc__, type(e), sep='\n')

            continue
        # Save the data to the file
    elif menu_choice == '3':
        # file = open(FILE_NAME, "w")
        # for student in students:
        #     file.write(f'{student["FirstName"]},{student["LastName"]},{student["GPA"]}\n')
        # file.close()
        # print("Data Saved!")
        # continue
        # out of the while loop
        # Exit the program
        try:
            file=open(FILE_NAME, "w")
            json.dump(students,file)
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("--Technical Error Message--")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("--Technical Error Message--")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file is not None and file.closed == False:
                file.close()
        continue
    elif menu_choice == "4":
        break  # out of the while loop