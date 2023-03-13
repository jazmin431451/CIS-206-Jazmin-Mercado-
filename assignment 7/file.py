"""This program file creation
It creates a file and adds password to the file
Input: none
Output:
	password: ask the user's password
	filename: writing the password in text into the file
References:
	https://www.geeksforgeeks.org/file-handling-python/
	https://en.wikiversity.org/wiki/Applied_Programming/Files/Python3
	https://en.wikipedia.org/wiki/Password_strength#Password_creation
	https://www.w3schools.com/python/python_file_handling.asp
	https://www.py4e.com/lessons/files
    https://en.wikipedia.org/wiki/Password_strength
    stratford career institute-13
"""
import math
import string
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
        return None
    else:
        return password


def calculate_entropy(password):
    """Calculates the entropy of a password.
    Args:
        password (string): Password to calculate entropy for.
    Returns:
        float: Entropy of the password strength.
    """
    length = len(password)
    character = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    number_possible_character = len(character)
    
    # Calculate the entropy using the formula E = log2(RL)
    entropy = math.log2(number_possible_character ** length)
    
    # Determine password strength based on entropy
    if entropy <= 28 :
        return 'weak'
    elif entropy <= 35 :
        return 'medium'
    elif entropy <= 59:
        return 'strong'
    else:
        return 'very strong'
        

def read_file(filename):
    """Reads filename and displays the file contents.
    Args:
        filename (string): Filename to open and read.
    Returns:
        None
    """
    with open(filename, "r") as file:
        print(file.read())


def append_file(filename, password):
    """Appends the password to the file.
    Args:
        filename (string): Filename to open and append.
        password (string): Password to append to the file.
    Returns:
        None
    """
    with open(filename, "a+") as f:
        f.write(password + "\n")


def main():  # pragma: no cover
    """Runs the main program logic."""
    filename = "file.txt"

    while True:
        password = get_password()
        if not password:
            break

        entropy = calculate_entropy(password)
        print(f"Password strength: {entropy}")

        read_file(filename)
        append_file(filename, password)


if __name__ == "__main__":  # pragma: no cover
    main()
