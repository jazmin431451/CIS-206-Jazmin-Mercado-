import pytest
import assignment_6


def test_get_text_returns_valid_input():
    input_values = ['test']

    def input(prompt=None):
        return input_values.pop(0)

    assignment_6.input = input
    assert assignment_6.get_text() == "test"


def test_get_text_empty_string_returns_none():
    input_values = ['']

    def input(prompt=None):
        return input_values.pop(0)

    assignment_6.input = input
    assert assignment_6.get_text() == None


def test_assignment_6_encode_rle_value_is_correct():
    assert assignment_6.encode_rle("") == ""
    assert assignment_6.encode_rle("a") == "a"
    assert assignment_6.encode_rle("aa") == "a2"
    assert assignment_6.encode_rle("abc") == "abc"
    assert assignment_6.encode_rle("abbc") == "ab2c"
    assert assignment_6.encode_rle("aaabcc") == "a3bc2"
    assert assignment_6.encode_rle("aaaaaaaaaa") == "a10"


def test_assignment_6_decode_rle_value_is_correct():
    assert assignment_6.decode_rle("") == ""
    assert assignment_6.decode_rle("a") == "a"
    assert assignment_6.decode_rle("a2") == "aa"
    assert assignment_6.decode_rle("abc") == "abc"
    assert assignment_6.decode_rle("ab2c") == "abbc"
    assert assignment_6.decode_rle("a3bc2") == "aaabcc"
    assert assignment_6.decode_rle("a10") == "aaaaaaaaaa"
