# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   JBoardman, 8/6/2024, updated script to add classes and functions and SOC
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
FILE_NAME: str = "Enrollments.json"
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

# Define the Data Variables and constants
menu_choice: str  # Hold the choice made by the user.
students: list = []  # a table of student data

# (jnb 8.6.24) removing these variables and will call them locally
# student_first_name: str = ''  # Holds the first name of a student entered by the user.
# student_last_name: str = ''  # Holds the last name of a student entered by the user.
# course_name: str = ''  # Holds the name of a course entered by the user.
# student_data: dict = {}  # one row of student data (jnb 8.6.24 replaced with student_new)
# csv_data: str = ''  # Holds combined string data separated by a comma. (jnb 8.6.24 not used)
# json_data: str = ''  # Holds combined string data in a json format. (jnb 8.6.24 not used)
# file = None  # Holds a reference to an opened file.

# Data --------------------------------------- #


class FileProcessor:
    """
    A collection of processing layer functions that work with Json files
    ChangeLog: (Who, When, What)
    JBoardman, 8.6.2024, created class and functions
    """
    # (jnb 8.6.24) When the program starts, read the file data into a list of lists (table)
    # (jnb 8.6.24) Extract the data from the file
    # (jnb 8.6.24) Call errors from IO.output_error_messages
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        Reads data from json file and returns it as a list
        ChangeLog: (Who, When, What)
        JBoardman, 8.6.2024, create function
        """
        # (jnb 8.6.24) Variables inside of this function
        file = None  # Holds a reference to an opened file.

        try:
            file = open(file_name, "r")  # (jnb 8.6.24) using variable file_name v file
            student_data = json.load(file)  # (jnb 8.6.24) using variable student_data v students
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("JSON file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with reading the file.\n\
            Please check that the file exists and that it is in a json format.", e)
        finally:
            if not file.closed:
                file.close()
        return student_data

    # (jnb 8.6.24) Write data to the json file
    # (jnb 8.6.24) Call errors from IO.output_error_messages
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        Writes data to json file
        ChangeLog: (Who, When, What)
        JBoardman, 8.6.2024, created function
        """
        # (jnb 8.6.24) Variables inside of this function
        file = None  # Holds a reference to an opened file.

        try:
            file = open(file_name, "w")  # (jnb 8.6.24) using variable file_name v file
            json.dump(student_data, file)  # (jnb 8.6.24) using variable student_data v students
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output
    ChangeLog: (Who, When, What)
    JBoardman, 8.6.2024, created class and functions
    """
    # (jnb 8.6.24) Variables inside of this class
    new_student: dict = {}  # one row of student data used in input_student_data function
    student_first_name: str = ''  # Holds the first name of a student entered by the user.
    student_last_name: str = ''  # Holds the last name of a student entered by the user.
    course_name: str = ''  # Holds the name of a course entered by the user.

    # (jnb 8.6.24) created function to be called for any error handling messages
    @staticmethod
    #  check if this works for file not found
    def output_error_messages(message: str, error: Exception = None):
        """
        Formats the error message and prints on screen
        ChangeLog: (Who, When, What)
        JBoardman, 8.6.2024, created function
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    # (jnb 8.6.24) created function to display menu output
    @staticmethod
    def output_menu(menu: str):
        """
        Display menu on screen
        ChangeLog: (Who, When, What)
        JBoardman, 8.6.2024, created function
        """
        # (jnb 8.6.24) Present the menu of choices
        print()  # (jnb 8.6.24) empty line for visual
        print(MENU)
        print()  # (jnb 8.6.24) empty line for visual

    # (jnb 8.6.24) created function to collect menu input and validate 1-4
    @staticmethod
    def input_menu_choice():
        """
        Collect input from user from menu
        ChangeLog: (Who, When, What)
        JBoardman, 8.6.2024, created function
        """
        menu_choice = "0"  # (jnb 8.6.24) No sure what this does need to test
        try:
            menu_choice = input("What would you like to do: ")
            if menu_choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  #(jnb 8.6.24) similar to Lab, avoids technical message
        return menu_choice

    # (jnb 8.6.24) created function to output current students list
    @staticmethod
    def output_student_courses(student_data: list):
        """
        Display Student data on screen
        ChangeLog: (Who, When, What)
        JBoardman, 8.6.2024, created function
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    # (jnb 8.6.24) created function to collect inputs from user
    @staticmethod
    def input_student_data(student_data: list):
        """
        Collect Student data from user
        ChangeLog: (Who, When, What)
        JBoardman, 8.6.2024, created function
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            new_student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(new_student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(e)  # (jnb 8.6.2024) printing only the value error message
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with your entered data.", e)
        return student_data  # (jnb 8.6.2024) added return for student data
#  End of function definitions


# Beginning of the main body of this script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)


# Present and Process the data
while True:
    # (jnb 8.6.2024) display the menu
    IO.output_menu(menu=MENU)

    # (jnb 8.6.2024) collect menu input
    menu_choice = IO.input_menu_choice()

    # (jnb 8.6.2024) Process inputs
    # (jnb 8.6.2024) Present the current data
    if menu_choice == "1":  # Get new data (and display the change)
        students = IO.input_student_data(student_data=students)
        #IO.output_student_courses(student_data=students)  # (jnb 8.6.24) similar to Lab3 for UX, removed
        continue

    # (jnb 8.6.2024) Present the current data
    elif menu_choice == "2":  # Display current data
        IO.output_student_courses(student_data=students)
        continue

    # (jnb 8.6.2024) Save the data to a file
    elif menu_choice == "3":  # Save data in a file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        print("The following data was saved to file!")  # (jnb 8.6.24) outside of the function for data processing
        IO.output_student_courses(student_data=students)
        continue

    # (jnb 8.6.2024) Stop the loop
    elif menu_choice == "4":  # End the program
        break  # out of the while loop
    else:
        print("Please only choose option 1, 2, or 3")

# (jnb 8.6.24) display when program ends
print("-" * 50)  # (jnb 8.6.24) for display only
print("Program Ended")
print("-" * 50)  # (jnb 8.6.24) for display only
