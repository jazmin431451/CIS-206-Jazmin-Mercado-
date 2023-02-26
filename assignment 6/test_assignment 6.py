import pytest
import assignment_6


def test_get_text_returns_valid_input():
    input_values = ['']

    def input(prompt=None):
        return input_values.pop(0)

    assignment_6.input = input
    assert assignment_6.get_text() == None


def test_get_text_empty_string_returns_none():
    input_values = ['']

    def input(prompt=None):
        return input_values.pop(0)

    assignment_6.input = input
    assert assignment_6.get_text() == None

def test_raises_encode_rle_value_error_numeric_value():
    with pytest.raises(Exception):
        assignment_6.encode_rle(float("X"))


def test_decode_rle_error_RLE_encoded_text():
    with pytest.raises(Exception):
        assignment_6.decode_rle("aaaaaabbbbccccc", "a6b4c5")

def test_assignment_6():
    assert assignment_6.encode_rle("aaaaabbbbbbcccc") == "a5b6c4"

def test_decode_rle_assertion_error_text():
    with pytest.raises(Exception):
        assignment_6.decode_rle("X", 'a3b4c2')


def test_get_text_assertion_error_isdigit():
    with pytest.raises(Exception):
        assignment_6.get_text('a3b4c2', "X")
