import pytest
import assignment_5


def test_get_pounds_returns_valid_input():
    input_values = ['100']

    def input(prompt=None):
        return input_values.pop(0)

    assignment_5.input = input
    assert assignment_5.get_pounds() == 100


def test_get_feet_return_valid_input():
    input_values = ['100']

    def input(prompt=None):
        return input_values.pop(0)

    assignment_5.input = input
    assert assignment_5.get_feet() == 100


def test_get_inches_return_valid_input():
    input_values = ['100']

    def input(prompt=None):
        return input_values.pop(0)

    assignment_5.input = input
    assert assignment_5.get_inches() == 100


def test_get_pounds_ignores_below_1000():
    input_values = ['1000.0', '0']

    def input(prompt=None):
        return input_values.pop(0)

    assignment_5.input = input
    assert assignment_5.get_pounds() == 1000.0


def test_get_feet_ignores_10():
    input_values = ['10', '0']

    def input(prompt=None):
        return input_values.pop(0)

    assignment_5.input = input
    assert assignment_5.get_feet() == 10


def test_get_inches_ignores_12():
    input_values = ['12', '0']

    def input(prompt=None):
        return input_values.pop(0)

    assignment_5.input = input
    assert assignment_5.get_inches() == 12


def test_get_pounds_ignores_string_values():
    input_values = ['error', '0']

    def input(prompt=None):
        return input_values.pop(0)

    assignment_5.input = input
    assert assignment_5.get_pounds() == 0


def test_get_feet_ignores_string_values():
    input_values = ['error', '0']

    def input(prompt=None):
        return input_values.pop(0)

    assignment_5.input = input
    assert assignment_5.get_feet() == 0


def test_get_inches_ignores_string_values():
    input_values = ['error', '0']

    def input(prompt=None):
        return input_values.pop(0)

    assignment_5.input = input
    assert assignment_5.get_inches() == 0


def test_get_pounds_empty_string_returns_none():
    input_values = ['']

    def input(prompt=None):
        return input_values.pop(0)

    assignment_5.input = input
    assert assignment_5.get_pounds() == None


def test_get_feet_empty_string_return_none():
    input_values = ['']

    def input(prompt=None):
        return input_values.pop(0)

    assignment_5.input = input
    assert assignment_5.get_feet() == None


def test_get_inches_empty_string_return_none():
    input_values = ['']

    def input(prompt=None):
        return input_values.pop(0)

    assignment_5.input = input
    assert assignment_5.get_inches() == None


def test_convert_height_inches():
    assert assignment_5.convert_height_inches(5, 3) == 63
    assert assignment_5.convert_height_inches(5, 2) == 62
    assert assignment_5.convert_height_inches(6, 3) == 75
    assert round(assignment_5.convert_height_inches(6, 4), 1) == 76


def test_calculate_bmi_empty_string_return_none():
    assert assignment_5.calculate_bmi(140, 63) == 24.8
    assert assignment_5.calculate_bmi(200, 62) == 36.6
    assert assignment_5.calculate_bmi(120, 75) == 15.0
    assert round(assignment_5.calculate_bmi(130, 76), 1) == 15.8


def test_calculate_bmi_raises_value_error_on_numeric_value():
    try:
        assignment_5.calculate_bmi(float("X"))

    except ValueError as error:
        print()
        print(error)


def test_calculate_bmi_value_error_positive_number():
    try:
        assignment_5.calculate_bmi(165, 62)

    except ValueError as error:
        print()
        print(error)


def test_display_results_displays_results(capsys):
    try:
        assignment_5.display_results(186, 75)
        captured = capsys.readouterr()
        assert captured.out == "140 pounds is 24.8 bmi\n\n"

    except AssertionError as error:
        print()
        print(error)


def test_display_results_raises_assertion_error_bmi():
    try:
        assignment_5.display_results("X", 0)

    except AssertionError as error:
        print()
        print(error)


def test_display_results_raises_assertion_error_classification():
    try:
        assignment_5.display_results(0, "X")

    except AssertionError as error:
        print()
        print(error)
