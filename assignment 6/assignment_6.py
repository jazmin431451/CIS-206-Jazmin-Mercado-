"""This program encodes and decodes strings using run-length encoding (RLE).
Input:
    Text string
Output:
    Encoded or decoded string
Example:
    Enter a string or press <Enter> to quit:
     AAABCC
    The encoded string is A3BC2.
    Enter a string or press <Enter> to quit:
    ...
References:
    https://en.wikipedia.org/wiki/Run-length_encoding
"""
import sys

def get_text():
    """
    Prompt the user to enter some text and return it.
    If the user enters an empty string, return None.
    """
    text = input("Enter some text: ")
    return text if text != '' else None


def encode_rle(text):
    """Run-length encodes text.

    Args:
        text (string): text to be encoded.

    Returns:
        encoded_text (string): RLE encoded text.

    """
    if not text:
        return ''

    encoded_text = ''
    current_char = text[0]
    count = 1

    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            encoded_text += current_char + (str(count) if count > 1 else '')
            current_char = text[i]
            count = 1

    encoded_text += current_char + (str(count) if count > 1 else '')

    return encoded_text

def decode_rle(text):
    """Run-length decodes text.

    Args:
        text (string): text to be decoded.

    Returns:
        decoded_text (string): RLE decoded text.

    """
    if not text:
        return ''
    decoded_text = ''
    current_char = ''
    count_str = ''
    for char in text:
        if char.isalpha():
            decoded_text += current_char * (int(count_str) if count_str else 1)
            current_char = char
            count_str = ''
        else:
            count_str += char

    decoded_text += current_char * (int(count_str) if count_str else 1)

    return decoded_text


def main():  # pragma: no cover
    """Runs the main program logic."""

    try:
        while True:
            text = get_text()
            if text == None:
                break
            print(f"You entered {encode_rle(text)}.")
            print("Here is your decoded string:\n")
            print(decode_rle(text))
    except:
        print("Unexpected error.")
        print("Error:", sys.exc_info()[1])
        print("File: ", sys.exc_info()[2].tb_frame.f_code.co_filename) 
        print("Line: ", sys.exc_info()[2].tb_lineno)


if __name__ == "__main__":  # pragma: no cover
    main()
