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


def encode_rle(text):
    """Run-length encodes text.

    Args:
        text (string): text to be encoded.

    Returns:
        encoded_text (string): RLE encoded text.

    """
    encoded_text = ""
    count = 0
    for i in range(0, len(text)):
        count += 1
        if i + 1 == len(text) or text[i] != text[i + 1]:
            encoded_text += text[i]
            if count != 1:
                encoded_text += str(count)
            count = 0
    return encoded_text


def decode_rle(text):
    """Run-length decodes text.

    Args:
        text (string): text to be decoded.

    Returns:
        decoded_text (string): RLE decoded text.

    """
    decoded_text = ""
    for i in range(len(text)):
        if text[i].isdigit():
            decoded_text += text[i - 1] * int(text[i])
        elif not text[i].isdigit():
            decoded_text += text[i]
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
