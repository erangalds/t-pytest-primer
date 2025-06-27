import pytest

def add(a, b):
    return a + b

@pytest.mark.parametrize("num1, num2, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (10, -5, 5),
    (0.1, 0.2, 0.3)
])
def test_add_function(num1, num2, expected):
    assert add(num1, num2) == pytest.approx(expected)

# You can also use pytest.param to add custom IDs or markers to individual parameter sets
@pytest.mark.parametrize("base, exponent, expected", [
    pytest.param(2, 3, 8, id="two_cubed"),
    pytest.param(5, 0, 1, id="any_number_to_power_zero"),
    pytest.param(10, 1, 10, id="any_number_to_power_one"),
    pytest.param(4, 0.5, 2, id="square_root", marks=pytest.mark.skip(reason="sqrt not yet implemented"))
])
def test_power_function(base, exponent, expected):
    # For simplicity, assuming a power function exists
    assert base ** exponent == expected