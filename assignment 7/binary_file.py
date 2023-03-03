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


def get_file():
	"""Obtains user input for file name

	Input: None

	Returns:
		file: string

	Except:
		ValueError: If file is not a valid string

	Exit:
		file is empty

	"""
	try:
		print('Please input the password you would like to use. To exit, press Enter')
		file = input()

		if type(file) is not str:
			raise ValueError

		if file == '':
			sys.exit(0)
		else:
			return file
	except ValueError:
		print("File name must be a string.")
		print("ValueError: '%s' is invalid." % file)


def append_characters(file):
	"""Fills file with the upper case english alphabet characters

	Input:
		file: string

	Output: None

	Exits:
		ValueError: If filename is not a valid string
		ValueError: If filename is an empty string

	"""

	try:
		fd_out = open(file, "wb+")

		if type(file) is not str:
			raise ValueError("File name must be a string.\nReceived %f" % file)
		if file == '':
			raise ValueError("File name cannot be empty.")

		id = 65
		val = id

		for i in range(26):
			entry = struct.pack('<HI', id, val)
			id += 1
			val = id

			fd_out.write(entry)
			fd_out.flush()

		fd_out.close()
	except:
		print("Unexpected error.")
		print("Error:", sys.exc_info()[1])
		print("File: ", sys.exc_info()[2].tb_frame.f_code.co_file)
		print("Line: ", sys.exc_info()[2].tb_lineno)


def main():
	"""Runs the main program logic."""

	try:
		file = get_file()
		append_characters(file)
	except:
		print("Unexpected error.")
		print("Error:", sys.exc_info()[1])
		print("File: ", sys.exc_info()[2].tb_frame.f_code.co_file)
		print("Line: ", sys.exc_info()[2].tb_lineno)


if __name__ == "__main__":
	main()
