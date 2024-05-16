# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   <kamal>,<05/15/2024>, <Assignment 5 Script>
# ------------------------------------------------------------------------------------------ #

from typing import IO # Defining Libraries
import json        # Defining Libraries

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
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"


# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
json_data: str = ''  # Holds combined string
student_data: dict[str, str] = {}  # dictionary for student
students: list = []  # a table of student data
# csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

# Error Handling to check if the file exists
try:
    file = open(FILE_NAME, 'r')
    students = json.load(file)
    file.close()
except Exception as e:
    print("Error: There was a problem opening the file.")
    print("Please check the file exist and try again.")
    print(e.__doc__)

finally:
    if file.closed == False:
        file.close()
        print("The file has been closed.")

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Student First Name must be alphabets.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Student Last Name must be alphabets.")
            course_name = input("Enter the course's name: ")
            student_data ={'FirstName': student_first_name,
                           'LastName': student_last_name,
                           'CourseName': course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

        except ValueError as e:
            print(e)
            print("Please try again.")

        except Exception as e:
            print(e)
            print("Please try again.")
           # print(e.__doc__)
           # print(e._str_())
        continue


    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]}'
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
            print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, 'w')
            json.dump(students, file)
            file.close()
            print("The file has been saved.")
            print("-" * 50)

            # to print all the data present in the file

            json_data = json.dumps(students)
            print(json_data)


            #for student in students:
            #    print(f'Student {student['FirstName']}'
            #        f'{student["LastName"]} is enrolled in {student["Course"]}')
        except Exception as e:
            print(e)
            if file.closed == False:
                file.close()
                print("The file has been closed.")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
