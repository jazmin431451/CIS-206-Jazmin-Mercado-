import sys
import struct


def get_password_strength(password):
	"""calculates the  password based on the length and the number of different character set used.

	Input: 
        password: The password to check.
	Returns:
		password: string

	Except:
		ValueError: If password is not a valid string

	Exit:
		filename is empty

	"""
	try:
		print('Please input the password would like to use. To exit, press Enter')
		password = input()

		if type(password) is not str:
			raise ValueError

		if password == '':
			sys.exit(0)
		else:
			return password
	except ValueError:
		print("password must be a string.")
		print("ValueError: '%s' is invalid." % password)
  
def append_characters(password):
	"""Fills password with the upper case english alphabet characters

	Input:
		password: string

	Output: None

	Exits:
		ValueError: If filename is not a valid string
		ValueError: If filename is an empty string

	"""

	try:
		pd_out = open(password, "wb")

		if type(password) is not str:
			raise ValueError("File name must be a string.\nReceived %f" % password)
		if password == '':
			raise ValueError("File name cannot be empty.")

		id = 65
		val = id

		for i in range(26):
			entry = struct.pack('<HI', id, val)
			id += 1
			val = id

			pd_out.write(entry)
			pd_out.flush()

		pd_out.close()
	except:
		print("Unexpected error.")
		print("Error:", sys.exc_info()[1])
		print("File: ", sys.exc_info()[2].tb_frame.f_code.co_filename)
		print("Line: ", sys.exc_info()[2].tb_lineno)
