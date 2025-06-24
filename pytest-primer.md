# `Pytest` Primer 

## Table of Contents
+ Module 1: Getting Started with `Pytest`
    + 1.1 What is `Pytest`
    + 1.2 Installation
    + 1.3 Basic Test Structure and Discovery
    + 1.4 Running tests
    + 1.5 Assertions
+ Module 2: Fixtures - Setup and Teardown

---

## Module 1: Getting Started with `Pytest`

Hey friends, getting to know a python based code testing framework was something I've been planning to do for a long time. But due to various reasons, I couldn't spend the time. But now the time has come, mainly because the need has come now. So I started to look around and found that `pytest` is one of the most widely used python testing frameworks. Therefore I thought of digging a little deeper into it to understand what it is and how does it work etc. This is what I learnt during that learning process.

### 1.1 What is `Pytest`
`Pytest` is a manture, full-featured python testing framework, that helps you to write simple yet scalable and maintainable test cases. But my first question was 

#### Why `Pytest`?
The reasons I found are as below. 
+ **Simple Syntax:** Very easy to get started, as it uses standard python `assert` statements. 
+ **Automatic Test Discovery:** Finds tests automatically based on naming conventions. 
+ **Fixtures:** Powerfull mechanism for test setup and teardown, promoting code reuse. 
+ **Parameterized Testing:** Run the same test with different inputs
+ **Extensible:** Rich plugin ecosystem
+ **Detailed Reporting:** Clear and readable output for test failures

### 1.2 Installation
Here is what I needed to get it installed. 

```bash
python -m pip install pytest
# Verify installation
pytest --version
```
### 1.3 Basic Test Structure and Discovery

Pytest follows specific conventions for test discovery:

- **Files**: Looks for files named `test_*.py` or `*_test.py`.
- **Functions**: Inside these files, it looks for functions named `test_*`.
- **Classes**: Inside these files, it looks for classes named `Test*` (without an `__init__` method), and methods within those classes named `test_*`.

Let me show you a very simple example. 

```python my_module.py 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```
using that module let me write the test file. 

```python test_my_module.py
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
    
```

### 1.4 Running tests

All I got to do now is 

```bash
pytest # Run all tests
pytest -v # verbose output 
pytest test_my_module.py # Run specific test file
pytest test_my_module.py::test_add_positive_numbers # Run specific test function
pytest test_my_module.py::TestAdvancedCalculations::test_add_zero # Run specific test class
pytest -k "add" # Run tests with keyword "add"
```
