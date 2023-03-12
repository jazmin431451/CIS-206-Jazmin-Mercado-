import pytest
import file

def test_get_password_returns_valid_input():
    input_values = ['rose']


    def input(prompt=None):
        return input_values.pop(0)


    file.input = input
    assert file.get_password() == "rose"


def test_get_password_ignores_string_value():
    input_value = ['rosemary1033']  

    def input(prompt=None):
        return input_value.pop(0)

    file.input = input
    assert file.get_password() == "rosemary1033"


def test_get_password_empty_string_returns_none():
    input_values = ['Rosemary1033@-@']


    def input(prompt=None):
        return input_values.pop(0)

 
    file.input = input
    assert file.get_password() == "Rosemary1033@-@"


def test__get_password_returns_password():
    assert file.get_password('semisoft') == "semisoft"
    assert file.get_password('semisoft+$$') == "semisoft+$$"
    assert file.get_password('semisoft+$$*-*') == "semisoft+$$*-*"
