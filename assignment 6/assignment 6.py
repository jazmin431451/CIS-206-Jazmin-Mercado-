"""This program counts thewoed in entered the stings.

Input: 
    text string

output:
    RLE encoded string 

Example:
    Enter a string or press <Enter> to quit:
    AAABC
    the user's enter A3BC2.
    enter a string or press <Enter> to quit:
    ...

References:
    https://https://en.wikiversity.org/wiki/Applied_Programming/Strings
"""

import sys

def get_text():
    """Gets text string.

    Args:
        None

    Returns:
        string: Text string entered or None if no string entered.

    """
    print("Enter a string or press <Enter> to quit:")
    text = input()
    if text == "":
        return None
    else:
        return text


def encode(text):
    """Encode a string using RLE.

    Args:
        text (string): Text string to be encoded.

    Returns:
        string: RLE encoded string.

    """
    encoded_string = ""
    current_char = text[0]
    count = 1
    for i in range(0, len(text)):
        if not current_char and text[i] not in encoded_string:
            count += 1  
        elif current_char and text[i] in encoded_string:
            count = 1
    return current_char

def decode(text):
    """Decodes a RLE encoded string.

    Args:
        text (string): RLE encoded string.

    Returns:
        string: Decoded string.

    """
    decoded_string = ""
    count = ""
    for i in range(len(text)):
        if text[i].isdigit():
            break    
        else: count += text[i]
    decoded_string = text[(count * 1): (len(text))]      
    return decoded_string

def main():
    """Runs the main program logic."""

    try:
        while True:
            text = get_text()
            if text == None:
                break
            print(f"You entered {decode(text)} decode.\n")
            print("Here is your string with the encode:\n")
            print(encode(text))
    except:
        print("Unexpected error.")
        print("Error:", sys.exc_info()[1])
        print("File: ", sys.exc_info()[2].tb_frame.f_code.co_filename) 
        print("Line: ", sys.exc_info()[2].tb_lineno)


main()
