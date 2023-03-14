import pytest
import file

def test_get_password_returns_valid_input():
    input_values = ['rose']

    def input(prompt=None):
        return input_values.pop(0)

    file.input = input
    assert file.get_password() == "rose"

def test_get_password_empty_string_returns_none():
    input_values = ['']

    def input(prompt=None):
        return input_values.pop(0)

    file.input = input
    assert file.get_password() == None

def test_calculate_entropy():
    assert file.calculate_entropy("j") == "weak"
    assert file.calculate_entropy("Isum4") == "medium"
    assert file.calculate_entropy("jelly22") == "strong"
    assert file.calculate_entropy("jelly22fish") == "very strong"
