"""This program demonstrates binary file creation

It creates a file and adds data to the file

Input: None

Output:
	upper_characters: file with the upper case english letters
	lower_characters: file with the lower case english letters

References:
	https://www.geeksforgeeks.org/file-handling-python/
	https://en.wikiversity.org/wiki/Applied_Programming/Files/Python3

"""

import sys
import struct

def get_file_name():
	"""Obtains user input for file name

	Input: None

	Returns:
		password: string

	Except:
		ValueError: If password is not a valid string

	Exit:
		password is empty

	"""
	try:
		
		print('Please input password you would like to use. To exit, press Enter')
		filename = input()

		if type(filename) is not str:
			raise ValueError

		if filename == '':
			sys.exit(0)
		else:
			return filename
	except ValueError:
		print("filename must be a strong.")
		print("ValueError: '%s' is invalid." % filename)


def append_characters(filename):
	"""Fills filename with the upper case english alphabet characters

	Input:
		filename: string

	Output: None

	Exits:
		ValueError: If filename is not a valid string
		ValueError: If filename is an empty string

	"""

	try:
		fd_out = open(filename, "wb+")
		if type(filename) is not str:
			raise ValueError("File name must be a string.\n Received %f" % filename)
		if filename == '':
			raise ValueError("File name cannot be empty.")
		length = (filename)
		character_sets += 26
		
		for i in range(60, 127):
			entry = struct.pack('<HI',filename)
			entry = length * (character_sets ** 2)
		
		fd_out.write(entry)
		fd_out.flush()

		fd_out.close()
	except:
		print("Unexpected error.")
		print("Error:", sys.exc_info()[1])
		print("File: ", sys.exc_info()[2].tb_frame.f_code.co_filename)
		print("Line: ", sys.exc_info()[2].tb_lineno)
		return entry
	
def load_words():
    with open('10-million-password.text') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def main():
	"""Runs the main program logic."""

	try:
		get_file_name()
		append_characters()
		load_words()
	except:
		print("Unexpected error.")
		print("Error:", sys.exc_info()[1])
		print("File: ", sys.exc_info()[2].tb_frame.f_code.co_filename)
		print("Line: ", sys.exc_info()[2].tb_lineno)

if __name__ == "__main__":
	main()
