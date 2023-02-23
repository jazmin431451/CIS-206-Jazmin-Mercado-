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

def test_raises_encoded_rle_value_error_numeric_value():
    with pytest.raises(ValueError):
        assignment_6.encoded_rle(float("X"))


def test_encoded_rle_raises_value_error_zero():
    with pytest.raises(ValueError):
        assignment_6.encoded_rle('a5b3c4')


def test_decoded_rle(capsys):
    assignment_6.decoded_rle('a3b4c2', 'aaabbbbcc')
    captured = capsys.readouterr()
    assert captured.out == "a3b4c2 encoded is aaabbbbcc decoded\n\n"


def test_decoded_rle_raises_assertion_error_text():
    with pytest.raises(AssertionError):
        assignment_6.display_results("X", 0)


def test_decoded_rle_raises_assertion_error_string():
    with pytest.raises(AssertionError):
        assignment_6.decode_rle(0, "X")
