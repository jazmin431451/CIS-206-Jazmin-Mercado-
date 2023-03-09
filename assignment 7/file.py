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

def get_password():
    """get the user enter the password.
    Args:
        password(str): The password input by the user, or True if the password is empty.
    Returns:
       float: password is weak or none if no password entered it return password.
    """
    print("Enter the password. To exit, press enter: ")
    password = input()
    
    if password == "":
        return True
    else:
        return password


def read_file():
    """Reads filename and displays the file contents.
    Args:
        filename (string): Filename to open and read.
    Returns:
        None
    """
    with open("file.txt", "r") as f:
        print(f.read())
    if 40 > 50:
        print("is reasonable password.")
    else:
        print("is strong passsword")

def append_file(filename, password):
    """Appends the password to the file.
    Args:
        filename (string): Filename to open and append.
        password (string): Password to append to the file.
    Returns:
        None
    """
    with open(filename, "a+") as f:
        f.write(password)


def main():
    """Runs the main program logic."""
    password = get_password()
    filename = "file.txt"

    while password != True:
        
        read_file()
        append_file(filename, password)
        password = get_password()


if __name__ == "__main__":
    main()
