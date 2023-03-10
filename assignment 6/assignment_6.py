"""This program file creation
It creates a file and adds password to the file
Input: none
Output:
	password: ask the user's password
	filename: writeing the password in text into the file
References:
	https://www.geeksforgeeks.org/file-handling-python/
	https://en.wikiversity.org/wiki/Applied_Programming/Files/Python3
	https://en.wikipedia.org/wiki/Password_strength#Password_creation
	https://www.w3schools.com/python/python_file_handling.asp
	https://www.py4e.com/lessons/files
    https://pymotw.com/2/re/
    stratford career institue your reading material - 2013
"""

import re
def get_password():
    """get the user enter the password.
    Args:
        password(str): The password input by the user, or True if the password is empty.
    Returns:
       float: password is weak or none if no password entered it return password.
    """
    print("Enter the password. To exit, press enter: ")
    password = input()
    if not password:
        return ''
    
def read_file(password):
    """Reads filename and displays the file contents.
    Args:
        filename (string): Filename to open and read.

    Returns:
        None
    """
    with open("file.txt", "r") as file:
        if re.search(password, file.read()):
            print("Password was found in the text file. Entropy: 0 to 32 bits.")  
            return 'weak'
    entropy = 0
    if any(character .islower() for character  in password):
        entropy += 4
    if any(character .isupper() for character  in password):
        entropy += 4
    if any(character .isdigit() for character  in password):
        entropy += 4
    if any(character  in "+,.:-_()*/;!?#" for character  in password):
        entropy += 6
    length = len(password)
    if length > 8:
        entropy += 12
    if length > 13:
        entropy += 20
    if length > 15:
        entropy += 24
    if length >= 20:
        entropy += 32

    if length > 1:
        entropy += (length - 1) * 2
    if length > 2:
        entropy += (length - 2) * 2
    if length > 3:
        entropy += (length - 3) * 2
    if entropy <= 4:
        return 'weak'
    elif entropy <= 12:
        return 'medium'
    elif entropy <= 24:
        return 'strong'
    else:
        return 'very strong'       
         
def append_file(filename, password):
    """Appends the password to the file.
    Args:
        filename (string): Filename to open and append.
        password (string): Password to append to the file.
    Returns:
        None
    """
    with open(filename, "a+") as file:
        file.write(password + '\n')


def main():
    """Runs the main program logic."""
    filename = "file.txt"

    while True:
        password = get_password()
        if not password:
            break
        print(f"Password strength: {password}")
        read_file()
        append_file(filename, password)

if __name__ == "__main__":
    main()
