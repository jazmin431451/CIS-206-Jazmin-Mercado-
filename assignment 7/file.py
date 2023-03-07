"""This program demonstrates binary file creation
It creates a file and adds data to the file
Input: None
Output:
	upper_characters: file with the upper case english letters
	lower_characters: file with the lower case english letters
References:
	https://www.geeksforgeeks.org/file-handling-python/
	https://en.wikiversity.org/wiki/Applied_Programming/Files/Python3
	https://en.wikipedia.org/wiki/Password_strength#Password_creation
"""
import os
import sys


def get_password():
    """Creates filename and adds temperature data to the file.

    Args:
        filename (string): Filename to create.

    Returns:
        None

    """
    password = input("enter the password. to exit, press enter")
    if password == "":
        return True
    else:
        return False
        

def create_file(file):
    """Reads filename and displays each line.

    Args:
        filename (string): Filename to open and read.

    Returns:
        None

    """
    with open(file, "w+") as password:
        password.write("the user passwor\n")
        for lenght in range(60, 127):
            password = 1 + lenght 
            password.write("the password has to be stronge .")
            
def read_file(file,):
    """Reads filename and displays each line.

    Args:
        filename (string): Filename to open and read.

    Returns:
        None

    """
    with open(file, "r+") as password:
        for line in password:
            line = line.strip()
            print(line)
    print("")
    with open("password-list-top.txt", "r+") as filename:
        print(filename)
    
    
def append_file(file):
    """Appends temperature data to filename.

    Args:
        filename (string): Filename to open and append.

    Returns:
        None

    """
    with open(file, "a+") as password:
        for lenght in range(127, 128):
            password = 1 + lenght 
            password.write("the password has to be stronge .")
            
def delete_file(filename):
    """Deletes filename.

    Args:
        filename (string): Filename to delete.

    Returns:
        None

    """
    os.remove(filename)

def main():
    """Runs the main program logic."""

    try:
        password = "file.text"
        filename = "password-list-top.text"

        if os.path.isfile(password):
            print("File '%s' already exists." % password)
            exit(1)
        get_password()
        create_file(password)
        read_file(password, filename)
        append_file(password)
        delete_file(password)
    except:
        print("Unexpected error.")
        print("Error:", sys.exc_info()[1])
        print("File: ", sys.exc_info()[2].tb_frame.f_code.co_filename) 
        print("Line: ", sys.exc_info()[2].tb_lineno)


main()
