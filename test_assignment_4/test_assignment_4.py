import pytest
from assignment_4 import pounds
from assignment_4 import feet
from assignment_4 import inches

def test_get_pounds_returns_valid_input():
   input_values = ['100']

   def input(prompt=None):
       return input_values.pop(0)

   pounds.input = input
   assert pounds.get_pounds() == 100
   
def test_get_feet_return_valid_input():
    input_values = ['100']
    
    def input(prompt=None):
        return  input_values.pop(0)
    
    feet.input = input
    assert feet.get_feet() == 100
    
def test_get_inches_return_valid_input():
    input_values = ['100']
    
    def input(prompt=None):
        return input_values.pop(0)
    inches.input = input
    assert inches.get_inches() == 100
    
def test_get_pounds_ignores_below_1000():  
    input_values = ['1000', '0']

    def input(prompt=None):
        return input_values.pop(0)
    
    pounds.input = input
    assert pounds.get_pounds() == 0

def test_get_feet_ignores_10():
    input_values = ['10', '0']
    
    def input(prompt=None):
        return input_values.pop(0)
    
    feet.input = input
    assert feet.get_feet() == 0
    
def test_get_inches_ignores_12():
    input_values = ['12', '0']
    
    def input(prompt=None):
        return input_values.pop(0)
    
    inches.input = input
    assert inches.get_inches() == 0  
    
def test_get_pounds_ignores_string_values():
    input_values = ['error', '0']
    
    def input(prompt= None):
        return input_values.pop(0)
    
    pounds.input = input
    assert pounds.get_pounds() == 0 
    
def test_get_feet_ignores_string_values():
    input_values = ['error', '0']
    
    def input(prompt=None):
        return input_values.pop(0)
    
    feet.input = input
    assert feet.get_feet() == 0
    
def test_get_inches_ignores_string_values():
    input_values = ['error', '0']
    
    def input(prompt=None):
        return input_values.pop(0)
    
    inches.input = input
    assert inches.get_inches() == 0
    
def test_get_pounds_empty_string_returns_none():
    input_values = ['']
    
    def input(prompt=None):
        return input_values.pop(0)
    
    pounds.input = input
    assert pounds.get_pounds() == None     
    
def test_get_feet_empty_string_return_none():
    input_values = ['']
    
    def input(prompt=None): 
        return input_values.pop(0)
    
    feet.input = input
    assert feet.get_feet() == None
    
def test_get_inches_empty_string_return_none():
    input_values = ['']
    
    def input(prompt=None):
        return input_values.pop(0)
    
    inches.input = input
    assert inches.get_inches() == None
    
def test_convert_height_inches(height_feet, height_inches):
    
    assert inches.convert_height_inches(5,3) == 63
    assert inches.convert_height_inches(5,2) == 62
    assert inches.convert_height_inches(6,3) == 75
    assert round(inches.convert_height_inches(6,4), 1) == 77

def test_calculate_bmi_empty_string_return_none():
    
    assert pounds.calculate_bmi(140) == 24.97
    assert pounds.calculate_bmi(200) == 36.84
    assert pounds.calculate_bmi(120) ==15.10
    assert round(pounds.calculate_bmi(130), 1) ==16.52
    
def test_convert_height_inches_raises_value_error_on_non_numeric_value():
    with pytest.raises(ValueError):
        inches.assignment_4(float("X"))
        
def test_calculate_bmi_raises_value_error_on_non_numeric_value():
    with pytest.raises(ValueError):
        pounds.calculate_bmi(float("X"))

def test_convert_height_inches_value_error_below_zero():
    with pytest.raises(ValueError):
        inches.covert_height_inches(6,3)

def test_calculate_bmi_value_error_below_zero():
    with pytest.raises(ValueError):
        pounds.calculate_bmi(130)

def test_display_results_display_bmi(bmi,classification):
    bmi.display_results(bmi > 0)
    captured = classification.readouterr()
    assert captured.out == "bmi pounds is 0 weight\n\n"


def test_display_results_raises_assertion_error_pounds():
    with pytest.raises(AssertionError):
        pounds.display_results("X", 0)


def test_display_results_raises_assertion_error_height_inches():
    with pytest.raises(AssertionError):
        inches.display_results(0, "X")    
