from my_module import add, subtract

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2

class TestAdvancedCalculations:
    def test_add_zero(self):
        assert add(2, 0) == 2

    def test_subtract_zero(self):
        assert subtract(5, 0) == 5
    
    def test_subtract_self(self):
        assert subtract(5, 5) == 0
