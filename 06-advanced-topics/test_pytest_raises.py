import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)

def test_divide_by_zero_specific_type():
    with pytest.raises(ZeroDivisionError): # This will fail, as we raise ValueError
        divide(10, 0)