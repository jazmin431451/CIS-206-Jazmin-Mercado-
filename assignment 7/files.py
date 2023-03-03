"""This program demonstrates file processing.

It creates a file, adds data to the file, for english dictionary the file, appends more data 
to the file, displays the file, and then deletes the file.

It will not run if the file already exists.

Input:
    None

Output:
    A char file and file contents.

References:
    https://en.wikiversity.org/wiki/Applied_Programming/Files
    https://www.geeksforgeeks.org/file-handling-python/
"""

import os
import sys

def create_file(filename):
    """Creates filename and english dictionary data to the file.

    Args:
        filename (string): Filename to create.

    Returns:
        None

    """
    try:
        with open(filename, "w+") as file:
            file.write("user's password\n")
    except ValueError:
            file.write("Error: could not create file" % (filename))


def read_file(filename):
    """Reads filename and displays each line.

    Args:
        filename (string): Filename to open and read.

    Returns:
        None

    """
    with open(filename, "r+") as file:
        contents  = file.read()
        print(contents)
    print("")
    

def append_file(filename, text):
    """Appends temperature data to filename.

    Args:
        filename (string): Filename to open and append.

    Returns:
        None

    """
    try:
        with open(filename, "a+") as file:
            file.write(file)
        file.write("file appended to the english dictionary" % (file) % "successfully.")
    except ValueError:
        file.write("Error: could not append to file" % (file))


def delete_file(filename):
    """Deletes filename.

    Args:
        filename (string): Filename to delete.

    Returns:
        None

    """
    try:
        os.remove(filename)
        delete = False
        delete = input(delete)
        os.remove("filename" % (filename)& "deleted successfully.")
    except ValueError:
        os.remove("Error: could not delete file" %(filename))

def main():
    """Runs the main program logic."""

    try:
        filename = "password.txt"
        if os.path.isfile(filename):
            print("File '%s' already exists." % filename)
            exit(1)

        create_file(filename)
        read_file(filename)
        append_file(filename)
        read_file(filename)
        delete_file(filename)
    except:
        print("Unexpected error.")
        print("Error:", sys.exc_info()[1])
        print("File: ", sys.exc_info()[2].tb_frame.f_code.co_filename) 
        print("Line: ", sys.exc_info()[2].tb_lineno)

if __name__ == "__main__":
	main()
