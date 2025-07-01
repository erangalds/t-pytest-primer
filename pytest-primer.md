# `Pytest` Primer 

## Table of Contents
+ Module 1: Getting Started with `Pytest`
    + 1.1 What is `Pytest`
    + 1.2 Installation
    + 1.3 Basic Test Structure and Discovery
    + 1.4 Running tests
    + 1.5 Assertions
+ Module 2: Fixtures - Setup and Teardown
    + 2.1 What are Fixtures?
    + 2.2 Basic Example of a Fixture
    + 2.3 Fixture Scope


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
### 1.5 Assertions
The reason why this has become very easy to use is because it uses the python `assert` statement. When an `assertion` fails, `pytest` provides detailed "assertion introspection", which is incredibly helpful for debugging.

Let me show you, how to use this *python* statement without `pytest`. 

```python
# Let us do a simple example assertion test
a = 10
b = 20
assert a == b, "a and b should be equal" # This will fail and show the values of a and b

# Lets do another example
my_list = [1, 2, 3, 4]
assert 5 in my_list, "5 should be in the list" # This message will be displayed when the assertion fails
```

Above, I showed you two simple examples of using *python* `assert` statement. Basically I showed you two tests. Now if we are to automate this we should be able to give a name to both of those tests. Assume below. 

```python
# equality test
a = 10
b = 20
assert a == b, "a and b should be equal" # This will fail and show the values of a and b

# list contains
my_list = [1, 2, 3, 4]
assert 5 in my_list, "5 should be in the list" # This message will be displayed when the assertion fails
```
I just used a comment line to give a name to the test. But when we want to automate tests, and check which ones succeeds and which ones fail, we need a better way to name the tests. Therefore, when we use `pytest` what we need to do is below. Only change that we have do is instead of using a comment, we make that a python function with a prefix `test_`. That's it, easy right. 

```python
def test_equality():
    a = 10
    b = 20
    assert a == b, "a and b should be equal" # This will fail and show the values of a and b

def test_contains():
    my_list = [1, 2, 3, 4]
    assert 5 in my_list, "5 should be in the list" # This message will be displayed when the assertion fails

def test_true_false():
    is_active = False
    assert is_active is True, "User should be active"
```

## Module 2: Fixtures - Setup and Teardown

### 2.1 What are Fixtures?
This is another useful feature of `pytest`. Fixtures are functions that pytest runs _before_ (and sometimes _after_) your tests to set up the environment or data needed for your tests. They promote reusability and help maintain consistent test conditions.

### 2.2 Basic Example of a Fixture
Let me show you a very basic example of a fixture. 

Use the `@pytest.fixture` decorator to define a fixture. Tests request fixtures by listing them as arguments in their function signature.

**`conftest.py`** (Conventionally, fixtures shared across multiple test files are placed in `conftest.py`)

```python conftest.py
import pytest

@pytest.fixture
def sample_data():
    """A simple list of numbers for testing."""
    return [1, 2, 3, 4, 5]

@pytest.fixture
def empty_list():
    """An empty list."""
    return []
```

Now let's look at how to use this in our tests. 

```python test_list_operations.py
def test_list_length(sample_data):
    assert len(sample_data) == 5

def test_list_sum(sample_data):
    assert sum(sample_data) == 15

def test_empty_list_length(empty_list):
    assert len(empty_list) == 0
```

What I found is that we need to keep the fixture configuration and the test file needs to be present in the same folder. To run the test we can easily to the below. 

```bash
pytest -x test_list_operations.py
```

### 2.3 Fixture Scope

Well, now next thing to know, is that *fixtures* can have different scopes. That determines how often they are run:
    + **function (default)**: Runs once per test function.
    + **class**: Runs once per test class.
    + **module**: Runs once per test module.
    + **session**: Runs once per test session.

Right, let's see this now. 

```python
# conftest.py
import pytest

@pytest.fixture(scope="session")
def db_connection():
    print("\nSetting up database connection (session scope)")
    # Simulate connection
    conn = "Database_Connection_Object"
    yield conn  # Provide the fixture value
    print("Closing database connection (session scope)")
    # Simulate teardown

@pytest.fixture(scope="module")
def api_client():
    print("Setting up API client (module scope)")
    # Simulate API client setup
    client = "API_Client_Object"
    yield client
    print("Closing API client (module scope)")

@pytest.fixture(scope="class")
def user_data():
    print("Setting up user data (class scope)")
    data = {"username": "testuser", "password": "password123"}
    yield data
    print("Cleaning up user data (class scope)")

@pytest.fixture(scope="function")
def temp_file(tmp_path): # tmp_path is a built-in pytest fixture
    print("Creating temporary file (function scope)")
    file = tmp_path / "test.txt"
    file.write_text("hello world")
    yield file
    print("Deleting temporary file (function scope)")

# test_scopes.py
import pytest

def test_db_read(db_connection):
    print(f"Test 1 using {db_connection}")
    assert True

def test_db_write(db_connection):
    print(f"Test 2 using {db_connection}")
    assert True

class TestAPI:
    def test_get_users(self, api_client, user_data):
        print(f"Test 3 using {api_client} and {user_data}")
        assert True

    def test_create_user(self, api_client, user_data):
        print(f"Test 4 using {api_client} and {user_data}")
        assert True

def test_file_content(temp_file):
    print(f"Test 5 using {temp_file}")
    assert temp_file.read_text() == "hello world"

def test_file_size(temp_file):
    print(f"Test 6 using {temp_file}")
    assert temp_file.stat().st_size > 0
```

Let's walk through how `pytest` executes our `test_scopes.py` file using the fixtures from `[conftest.py]`. Think of the scopes as nested layers, from the largest to the smallest: `session` -> `module` -> `class` -> `function`.

#### The Execution Flow Step-by-Step

##### Analysis of Your Output

Here is the step-by-step breakdown of what `pytest` is doing:

1. **`pytest` starts the session.** It looks at the first test and sees that the `db_connection` fixture (scope: `session`) will be needed. Since it's a session-scoped fixture, `pytest` sets it up immediately to be available for the entire run.
    
    - **OUTPUT:** `Setting up database connection (session scope)`
2. **`pytest` runs `test_db_read`.** This is the first test.
    
    - It requests `db_connection`. `pytest` has this ready from Step 1 and provides it.
    - **OUTPUT:** `Test 1 using Database_Connection_Object`
3. **`pytest` runs `test_db_write`.**
    
    - It also requests `db_connection`. `pytest` provides the _same cached object_ from Step 1.
    - **OUTPUT:** `Test 2 using Database_Connection_Object`
4. **`pytest` moves to the `TestAPI` class and prepares to run `test_get_users`.**
    
    - This is the **first time** any test has requested the `api_client` fixture. Since its scope is `module`, `pytest` executes its setup code now.
    - **OUTPUT:** `Setting up API client (module scope)`
    - This is also the **first time** any test has requested the `user_data` fixture. Since its scope is `class`, `pytest` executes its setup code now.
    - **OUTPUT:** `Setting up user data (class scope)`
    - Now that all dependencies are met, the test runs.
    - **OUTPUT:** `Test 3 using API_Client_Object and {'username': 'testuser', 'password': 'password123'}`
5. **`pytest` runs `test_create_user`.**
    
    - It requests `api_client` and `user_data`. `pytest` provides the cached versions that were set up in the previous step. The test runs.
    - **OUTPUT:** `Test 4 using API_Client_Object and {'username': 'testuser', 'password': 'password123'}`
6. **`pytest` finishes the `TestAPI` class.**
    
    - The scope of the `user_data` fixture is now over. `pytest` runs its teardown code.
    - **OUTPUT:** `Cleaning up user data (class scope)`
7. **`pytest` runs `test_file_content`.**
    
    - This is the first time it sees a request for `temp_file` (scope: `function`). It runs the setup.
    - **OUTPUT:** `Creating temporary file (function scope)`
    - The test runs.
    - **OUTPUT:** `Test 5 using ...`
    - The function is over, so the `function` scope ends. `pytest` immediately runs the teardown.
    - **OUTPUT:** `Deleting temporary file (function scope)`
8. **`pytest` runs `test_file_size`.**
    
    - It again requests `temp_file`. Because the scope is `function`, the fixture is created anew.
    - **OUTPUT:** `Creating temporary file (function scope)`
    - The test runs, and the teardown follows immediately.
    - **OUTPUT:** `Test 6 using ...`
    - **OUTPUT:** `Deleting temporary file (function scope)`
9. **`pytest` finishes the `test_scopes.py` module.**
    
    - The scope of the `api_client` fixture is now over. `pytest` runs its teardown.
    - **OUTPUT:** `Closing API client (module scope)`
10. **`pytest` finishes the entire session.**
    
    - The scope of the `db_connection` fixture is now over. `pytest` runs its teardown.
    - **OUTPUT:** `Closing database connection (session scope)`

##### Conclusion
The reason you see the `db_connection` setup before the `api_client` setup is simply because the first tests `pytest` decided to run (`test_db_read`, `test_db_write`) only needed the session-scoped fixture. The module-scoped `api_client` wasn't needed until later, so its setup was deferred until that point.

#### Execution order of the `test_scopes_different_class_first.py` file

Now the key difference is the order of tests in our new file, `test_scopes_different_class_first.py`. In this file, the `TestAPI` class appears before the standalone `test_db_*` functions. `Pytest` generally runs tests in the order they appear in the file.

Let's break down this new execution flow step-by-step.

##### Analysis of the New Execution Order

1. **`pytest` starts and discovers tests.** It begins with `[test_scopes_different_class_first.py](code-assist-path:/Users/eranga/Documents/my-trainings/t-pytest-primer/02-fixtures/fixture_scope/test_scopes_different_class_first.py "/Users/eranga/Documents/my-trainings/t-pytest-primer/02-fixtures/fixture_scope/test_scopes_different_class_first.py")` and finds the `TestAPI` class first.
    
2. **`pytest` prepares to run `test_get_users` (inside `TestAPI`).**
    
    - This is the **first time** a test in this module requires the `api_client` fixture. `pytest` executes its setup code now.
    - **OUTPUT:** `Setting up API client (module scope)`
    - This is also the **first time** a test in this class requires the `user_data` fixture. `pytest` executes its setup code.
    - **OUTPUT:** `Setting up user data (class scope)`
    - With the dependencies ready, the test runs.
    - **OUTPUT:** `Test 3 using API_Client_Object and {'username': 'testuser', 'password': 'password123'}`
3. **`pytest` runs `test_create_user`.**
    
    - It requests `api_client` and `user_data`, which are already cached from the previous step. The test runs.
    - **OUTPUT:** `Test 4 using API_Client_Object and {'username': 'testuser', 'password': 'password123'}`
4. **`pytest` finishes the `TestAPI` class.**
    
    - The scope for the `user_data` fixture is over, so its teardown code is executed.
    - **OUTPUT:** `Cleaning up user data (class scope)`
5. **`pytest` moves to the next test in the file, `test_db_read`.**
    
    - This is the **first time in the entire session** that a test has requested the `db_connection` fixture. Even though its scope is `session`, its setup was deferred until it was actually needed. `pytest` executes its setup now.
    - **OUTPUT:** `Setting up database connection (session scope)`
    - The test runs, using the newly created connection object.
    - **OUTPUT:** `Test 1 using Database_Connection_Object`
6. **`pytest` runs `test_db_write`.**
    
    - It requests `db_connection` and gets the cached session-scoped object.
    - **OUTPUT:** `Test 2 using Database_Connection_Object`
7. **`pytest` runs the `temp_file` tests.**
    
    - This part behaves identically to the previous run. For each of the two tests (`test_file_content` and `test_file_size`), the function-scoped `temp_file` fixture is set up and torn down.
    - **OUTPUT:**
        
        unfold_moreplaintext
        
        content_copyadd
        
         Show full code block 
        
        `Creating temporary file (function scope) Test 5 using ... .Deleting temporary file (function scope) Creating temporary file (function scope) Test 6 using ... .Deleting temporary file (function scope)`
        
8. **`pytest` finishes the module.**
    
    - The scope for the `api_client` fixture is now over, so its teardown runs.
    - **OUTPUT:** `Closing API client (module scope)`
9. **`pytest` finishes the entire session.**
    
    - Finally, the scope for the `db_connection` fixture is over, and its teardown runs.
    - **OUTPUT:** `Closing database connection (session scope)`

##### Conclusion

**The order of tests in your file dictates the order of "first use" for fixtures, which in turn dictates the setup order.**

Even though `db_connection` has the broadest scope (`session`), its setup was delayed until a test actually asked for it. Because the `TestAPI` tests ran first, the `module` and `class` scoped fixtures they needed were set up before the `session` scoped fixture.

### 2.4 `conftest.py` 
This special file located at the root of our test directory (or any subdirectory) automatically loads _fixtures_ defined within it, making them available to tests in that directory and its subdirectories. We don't need any explicit imports. 

### 2.6 Fixture Parameterization (params)

Next fun part is that we can parameterize fixtures. This allows us to run the fixture multiple times with different values. 


#### How it works. 

The files `conftest.py` and `test_web_app.py` demonstrate fixture parameterization in `pytest`. Let's break down how they work together and how to run the tests.

**`conftest.py` (Fixture Definition)**

- The `conftest.py` file defines a fixture named `browser`.
- `@pytest.fixture(params=["chrome", "firefox"], ids=["browser_chrome", "browser_firefox"])` This decorator makes `browser` a parameterized fixture.
    - `params=["chrome", "firefox"]`: This specifies the different values that the fixture will take. In this case, the fixture will run once with the value `"chrome"` and once with the value `"firefox"`.
    - `ids=["browser_chrome", "browser_firefox"]`: This provides human-readable names for each parameter set, which will appear in the test output.
- The fixture function `browser(request)` takes a special argument, `request`. This `request` object is a built-in `pytest` fixture that provides information about the current test being executed.
- `browser_name = request.param`: Inside the fixture, `request.param` accesses the current parameter value (either `"chrome"` or `"firefox"`).
- The fixture simulates setting up a browser (in reality, you might launch a browser here) and yields a string like `"Browser_Object_{browser_name}"`. This yielded value is what will be injected into the tests that use this fixture.
- After the test using the fixture completes, the code after `yield` simulates closing the browser.

**`test_web_app.py` (Test Usage)**

- The `test_web_app.py` file contains two test functions, `test_login_page` and `test_homepage`.
- Both test functions take `browser` as an argument. This tells `pytest` that these tests depend on the `browser` fixture.
- When `pytest` runs these tests, it will:
    1. Recognize that `browser` is a parameterized fixture.
    2. Run `test_login_page` twice:
        - Once with `browser` set to `"Browser_Object_chrome"`.
        - Once with `browser` set to `"Browser_Object_firefox"`.
    3. Similarly, run `test_homepage` twice with the same parameter values for `browser`.
- Inside the tests, the value of `browser` (e.g., `"Browser_Object_chrome"`) is used in a `print` statement, and the assertions are modified to always pass for demonstration purposes.

**How to Run the Tests**

To run these tests, you would typically execute `pytest` from the directory containing these files:

```bash
pytest
```

Because the `browser` fixture is parameterized, `pytest` will automatically run each test twice, once for each parameter value. The output will clearly indicate which browser is being used for each test run, thanks to the `ids` in the fixture definition.

If you want to run only the tests for a specific browser, you can use the `-k` option with a keyword expression:

```bash
pytest -k "browser_chrome"  # Run only tests with chrome 
pytest -k "browser_firefox" # Run only tests with firefox`
```

This command filters the tests based on the `ids` you provided in the fixture, ensuring that only the relevant tests are executed.

## Module 3: Parameterized Testing

### 3.1 `pytest.mark.parametrize`

This is a powerful decorator to run a single test function multiple times with different sets of input data. It significantly reduces code duplication. 

**Syntax**: `@pytest.mark.parametrize("arg1, arg2, ..., argN", [(val1a, val2a, ..., valNa), (val1b, val2b, ..., valNb), ...])`

Let me now show you an example. 

```python
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
```

**How it works**

**Core Concept**: `@pytest.mark.parametrize`

This decorator is the star of the show. It tells `pytest` to call a single test function multiple times, feeding it different arguments for each run.

**Analysis of `test_add_function`**

1. **`@pytest.mark.parametrize(...)`**: This decorator is applied to `test_add_function`.
2. **`"num1, num2, expected"`**: This string defines the names of the arguments that will be passed to the test function.
3. **`[...]`**: This list contains tuples. Each tuple represents one complete set of arguments for a single test run.
    - For the first run, `num1` will be `1`, `num2` will be `2`, and `expected` will be `3`.
    - For the second run, `num1` will be `-1`, `num2` will be `1`, and `expected` will be `0`.
    - ...and so on for all five tuples.
4. **`assert add(num1, num2) == pytest.approx(expected)`**: This is the test logic. It's executed for each set of parameters. The use of `pytest.approx()` is a crucial best practice for comparing floating-point numbers, as it checks if they are "close enough" rather than exactly equal, avoiding precision issues like the `0.1 + 0.2` problem.

In essence, we have written one test function that `pytest` automatically expands into five separate tests, each with different data.

**Analysis of `test_power_function`**

This test demonstrates a more advanced and descriptive way to parameterize using `pytest.param`.

Here, instead of simple tuples, each test case is wrapped in `pytest.param()`. This gives you extra capabilities:

- **`id="two_cubed"`**: This provides a custom, human-readable ID for the test case. In the test report, you'll see `PASSED test_power_function[two_cubed]` instead of a less descriptive default like `PASSED test_power_function[2-3-8]`. This makes debugging much easier.
- **`marks=pytest.mark.skip(...)`**: This allows you to apply a `pytest` marker (like `skip`, `xfail`, or custom markers) to a _single parameter set_. In this case, the "square_root" test is specifically marked to be skipped, while the other parameter sets for `test_power_function` will still run.

### 3.2 Combining Parameters with Fixtures

We can take this to another level by combining both the parameters and fixtures. Let me show you how to do that now. 

Fixture configuration. 

```python
# conftest.py
import pytest

@pytest.fixture(params=[10, 20], ids=["size_10", "size_20"])
def dataset_size(request):
    return request.param
```

Actual pytest file with parameters. 

```python
# test_data_processing.py
def process_data(data, size):
    return len(data) * size

@pytest.mark.parametrize("data_input", [
    ([1, 2]),
    ([1, 2, 3, 4])
], ids=["short_list", "long_list"])
def test_data_processing_with_size(dataset_size, data_input):
    expected_output = len(data_input) * dataset_size
    assert process_data(data_input, dataset_size) == expected_output
```

**How `conftest.py` and `test_data_processing.py` Work Together**

This pair of files demonstrates a very common and effective pattern in `pytest`: combining a parameterized fixture with a parameterized test function. This allows you to test a function with a matrix of different inputs.

**`conftest.py` - The Parameterized Fixture**

- **`@pytest.fixture(...)`**: This decorator marks `dataset_size` as a `pytest` fixture.
- **`params=[10, 20]`**: This is the key part for parameterization. It tells `pytest` that this fixture should be instantiated twice: once with the value `10` and once with the value `20`.
- **`ids=["size_10", "size_20"]`**: These are optional, human-readable identifiers for each parameter value. They make the test output much clearer, showing which specific parameter value is being used for a given test run (e.g., `test_data_processing_with_size[size_10-short_list]`).
- **`dataset_size(request)`**: The `request` object is a special built-in `pytest` fixture that provides information about the current test context.
- **`return request.param`**: This line retrieves the current parameter value (either `10` or `20`) and makes it available to any test that requests the `dataset_size` fixture. Since there's no `yield` statement, this is a simple "value-providing" fixture without any setup/teardown logic.

**In essence**: The `dataset_size` fixture will provide two distinct values (`10` and `20`) to any test that uses it.

**`test_data_processing.py]` - The Parameterized Test Function**

- **`process_data(data, size)`**: This is the function under test. It takes a list `data` and an integer `size`, and returns their product of `len(data)` and `size`.
- **`@pytest.mark.parametrize("data_input", ...)`**: This decorator parameterizes the `test_data_processing_with_size` function itself.
    - **`"data_input"`**: This is the name of the argument that will receive the parameterized values.
    - **`[([1, 2]), ([1, 2, 3, 4])]`**: These are the two different lists that `data_input` will take.
    - **`ids=["short_list", "long_list"]`**: Again, human-readable identifiers for these parameter sets.
- **`def test_data_processing_with_size(dataset_size, data_input):`**: This test function requests two arguments:
    - `dataset_size`: This is the parameterized fixture defined in `conftest.py`.
    - `data_input`: This is the parameterized argument defined by the `@pytest.mark.parametrize` decorator on the test function itself.
- **`expected_output = len(data_input) * dataset_size`**: Calculates the expected result based on the current `data_input` and `dataset_size`.
- **`assert process_data(data_input, dataset_size) == expected_output`**: The actual assertion, comparing the function's output with the expected value.

**In essence**: This test function will be run multiple times, once for each combination of `data_input` and `dataset_size`.

#### How They Work Together (The Cross-Product)

When you run `pytest` on `test_data_processing.py`, `pytest` sees that:

1. The `dataset_size` fixture has 2 parameters (`10`, `20`).
2. The `test_data_processing_with_size` test function has 2 parameters for `data_input` (`[1, 2]`, `[1, 2, 3, 4]`).

`pytest` will automatically create a "cross-product" of these parameters, meaning the test will run for every possible combination. In this case, `2 * 2 = 4` test runs will be generated:

1. `test_data_processing_with_size[size_10-short_list]`
    - `dataset_size` = `10`
    - `data_input` = `[1, 2]`
    - `process_data([1, 2], 10)` -> `2 * 10 = 20`
2. `test_data_processing_with_size[size_10-long_list]`
    - `dataset_size` = `10`
    - `data_input` = `[1, 2, 3, 4]`
    - `process_data([1, 2, 3, 4], 10)` -> `4 * 10 = 40`
3. `test_data_processing_with_size[size_20-short_list]`
    - `dataset_size` = `20`
    - `data_input` = `[1, 2]`
    - `process_data([1, 2], 20)` -> `2 * 20 = 40`
4. `test_data_processing_with_size[size_20-long_list]`
    - `dataset_size` = `20`
    - `data_input` = `[1, 2, 3, 4]`
    - `process_data([1, 2, 3, 4], 20)` -> `4 * 20 = 80`

This approach is incredibly powerful for thoroughly testing functions with various inputs and configurations without writing repetitive test code.

## Module 4: Markers - Organizing and Filtering Tests

### 4.1 What are Markers?

Markers are a way to tag or label your test functions with custom metadata. This allows you to selectively run or skip tests based on these tags.

### 4.2 Built-in Markers

`pytest` provides several built-in markers

- `@pytest.mark.skip(reason="...")`: Unconditionally skips a test.
- `@pytest.mark.skipif(condition, reason="...")`: Skips a test if the condition is true.
- `@pytest.mark.xfail(condition, reason="...")`: Marks a test as "expected to fail". If it fails, it's reported as `xfailed`. If it passes, it's reported as `xpassed`.
- `@pytest.mark.parametrize(...)`: (As covered in Module 3)


Let me show you these in action now. 

```python
import pytest
import sys

def test_always_runs():
    assert True

@pytest.mark.skip(reason="This test is temporarily disabled")
def test_disabled_feature():
    assert False # This will not run

@pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
def test_linux_only_feature():
    assert True

@pytest.mark.xfail(reason="Bug #123: This feature is currently broken")
def test_buggy_feature():
    assert 1 == 2 # This test is expected to fail
```

- `test_always_runs`: This is a basic test that will always pass, serving as a baseline.
- `@pytest.mark.skip(reason="This test is temporarily disabled")`: This marker will cause `test_disabled_feature` to be skipped. The test will not be executed, and the report will show it as skipped with the provided reason.
- `@pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")`: This marker conditionally skips `test_linux_only_feature`. The test will be skipped only if the condition `sys.platform == "win32"` is true (i.e., the test is run on a Windows machine). Otherwise, the test will be executed.
- `@pytest.mark.xfail(reason="Bug #123: This feature is currently broken")`: This marker marks `test_buggy_feature` as "expected to fail". If the test fails (as it's designed to do), it will be reported as `xfailed` (expected failed). If the test unexpectedly passes, it will be reported as `xpassed` (expected passed), which might indicate that the bug has been fixed and the test or the marker needs to be reviewed.

### 4.3 Custom Markers

We can define our own markers. These are useful when we have to categorize tests. 

**Step 1**:  Setting up the `pytest.ini` file. 


We need to setup a custom file `pytest.init` as below with the required configuration. 

```python
# pytest.ini
[pytest]
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    database: marks tests that interact with the database
    ui: marks tests related to the user interface
```

Then we need to mark the tests with those markers. 

**Step 2**: Marking the tests with markers

```python
import pytest 

@pytest.mark.slow
def test_performance_intensive():
    # Simulate a long-running operation
    import time 
    time.sleep(5)
    assert True 

@pytest.mark.database
def test_user_creation_in_db():
    # Connect to DB and create user
    assert True 

@pytest.mark.ui 
def test_login_button_visibility():
    # Check if login button is visible
    assert True 
```

**Step 4**: Running the tests

+ Run all tests: `pytest -v`
+ Run all `slow` tests: `pytest -v -m "slow"`
+ Run all `database` tests: `pytest -v -m "database"`
+ Run all `ui` tests: `pytest -v -m "ui"`
+ Run all `database` and 'ui' tests: `pytest -v -m "database or ui"`
+ Run all `database` but not `ui` tests: `pytest -v -m "database and not ui"`
+ Listing all registered markers: `pytest -v --markers`

### 4.4 Applying Markers to `Classes` and `Modules`

We can even apply markers to `classes` and `modules`. This makes easier, because then it gets applied to all tests within them. 

## Module 5: Mocking and Patching

### 5.1 What is Mocking? and Why Mock?
Mocking allows us to replace real objects with "fake" objects that simulate the behavior of the real ones. When testing code that interacts with external systems (databases, APIs, file systems, etc.), if we want to isolate our unit tests from these dependencies, we can use mocking. This gives us more control over their responses and side effects. 

### 5.2 `pytest-mock` Plugin

We need to use a separate plug for this. `pytest` doesn't come with a built-in capability. `pytest-mock` plugin which wraps python's `unittest.mock` library provides this functionality. 

We can install that separately as below. 

```bash
python -m pip install pytest-mock
```

Key features of `pytest-mock`
+ Provides a `mocker` fixture that automatically handles patching and unpatching
+ Simplified API for common mocking operations. 

```python
import smtplib

def send_welcome_email(recipient_email, message):
    try:
        # Simulate connecting to an SMTP server
        smtp_server = smtplib.SMTP('smtp.example.com', 587)
        smtp_server.starttls()
        smtp_server.login("user@example.com", "password")
        smtp_server.sendmail("sender@example.com", recipient_email, message)
        smtp_server.quit()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
```

Now let's look at our test file. 

```python
import pytest
import smtplib # <--- Add this line
from email_service import send_welcome_email

def test_send_welcome_email_success(mocker):
    # Mock the smtplib.SMTP class and its methods
    mock_smtp_class = mocker.patch('email_service.smtplib.SMTP')

    # Configure the mock instance that will be returned when SMTP is called
    mock_smtp_instance = mock_smtp_class.return_value
    mock_smtp_instance.starttls.return_value = None
    mock_smtp_instance.login.return_value = None
    mock_smtp_instance.sendmail.return_value = None
    mock_smtp_instance.quit.return_value = None

    result = send_welcome_email("test@example.com", "Welcome!")

    # Assert that the mocked methods were called as expected
    mock_smtp_class.assert_called_once_with('smtp.example.com', 587)
    mock_smtp_instance.starttls.assert_called_once()
    mock_smtp_instance.login.assert_called_once_with("user@example.com", "password")
    mock_smtp_instance.sendmail.assert_called_once_with("sender@example.com", "test@example.com", "Welcome!")
    mock_smtp_instance.quit.assert_called_once()
    assert result is True

def test_send_welcome_email_failure(mocker):
    # Mock the sendmail method to raise an exception
    mock_smtp_class = mocker.patch('email_service.smtplib.SMTP')
    mock_smtp_instance = mock_smtp_class.return_value
    mock_smtp_instance.sendmail.side_effect = smtplib.SMTPException("Connection error")

    result = send_welcome_email("test@example.com", "Welcome!")

    assert result is False
    mock_smtp_instance.sendmail.assert_called_once() # Still called, but raised an exception
```
**How this works**: 

1. `email_service.py`: The Code Under Test

This file contains a single function, `send_welcome_email`. Its purpose is to simulate sending an email using Python's built-in `smtplib` module.

- It attempts to establish a connection to an SMTP server (`smtplib.SMTP`).
- It starts TLS encryption (`starttls()`).
- It logs in with credentials (`login()`).
- It sends the email (`sendmail()`).
- It closes the connection (`quit()`).
- It returns `True` on success and `False` if any exception occurs during the process.

**The Challenge for Testing:** If you were to test `send_welcome_email` directly without any special tools, your tests would:

- Require a live SMTP server.
- Actually send emails (which you probably don't want during testing).
- Be slow and unreliable (dependent on network, server availability, etc.).

This is where `test_email_service.py` comes in, using **mocking** to overcome these challenges. Sounds nice right? 

2. `test_email_service.py`: Testing with Mocks

This file uses the `pytest-mock` plugin (which provides the `mocker` fixture) to replace parts of `smtplib` with "mock" objects during testing.

**Key Concepts** in :

1. **`mocker` Fixture**:
    
    - Provided by `pytest-mock`.
    - It's a wrapper around Python's `unittest.mock` library.
    - It automatically handles patching and unpatching, ensuring that your mocks are cleaned up after each test, preventing test interference.

2. **`mocker.patch('module.ClassOrFunction')`**:
    
    - This is the core of mocking. `mocker.patch()` replaces a specified object (a class, function, or attribute) with a mock object.
    - In both tests, `mocker.patch('email_service.smtplib.SMTP')` replaces the actual `smtplib.SMTP` class (as imported within `email_service.py`) with a mock. This means when `email_service.py` tries to create an `smtplib.SMTP` object, it gets our mock instead.

3. **`mock_smtp_class.return_value`**:
    
    - When you mock a class (like `smtplib.SMTP`), `mock_smtp_class` becomes a mock object that _represents the class itself_.
    - When `smtp_server = smtplib.SMTP(...)` is called in `email_service.py`, it's actually calling `mock_smtp_class(...)`.
    - `mock_smtp_class.return_value` is what the mock class will return when it's "instantiated" (i.e., when `smtplib.SMTP()` is called). By setting `mock_smtp_class.return_value` to another mock object (`mock_smtp_instance`), we can then control the methods of that "instance."

4. **`mock_smtp_instance.method.return_value = ...`**:
    
    - This sets the return value for a specific method on the mocked instance.
    - For example, `mock_smtp_instance.starttls.return_value = None` means that when `smtp_server.starttls()` is called, it will simply return `None` (simulating a successful operation that doesn't return anything meaningful).

5. **`mock_smtp_instance.method.side_effect = ...`**:
    
    - This is used to make a mocked method raise an exception or execute a custom function when called.
    - In `test_send_welcome_email_failure`, `mock_smtp_instance.sendmail.side_effect = smtplib.SMTPException("Connection error")` tells the mock `sendmail` method to raise an `SMTPException` when it's called. This simulates a network error or authentication failure.
    - **The `import smtplib` is needed even here because `smtplib.SMTPException` is a class from the `smtplib` module, and `test_email_service.py` needed direct access to it to set the `side_effect`.

6. **Assertion Methods on Mocks (`.assert_called_once_with()`, `.assert_called_once()`)**:
    
    - Mock objects automatically record how they are called.
    - `mock_smtp_class.assert_called_once_with('smtp.example.com', 587)` verifies that the `SMTP` class was instantiated exactly once with the specified arguments.
    - `mock_smtp_instance.starttls.assert_called_once()` verifies that the `starttls` method on the mock instance was called exactly once.
    - These assertions are crucial for ensuring that your code interacts with its dependencies in the way you expect, even if those dependencies are mocked out.

**Test Case Breakdown**:

- **`test_send_welcome_email_success(mocker)`**:
    
    - **Goal**: Verify that `send_welcome_email` works correctly when the underlying SMTP operations succeed.
    - **Mocking**: All methods (`starttls`, `login`, `sendmail`, `quit`) on the mocked `SMTP` instance are configured to return `None` (or a successful value).
    - **Assertion**: It checks that `send_welcome_email` returns `True` and that all expected `smtplib` methods were called exactly once with the correct arguments.

- **`test_send_welcome_email_failure(mocker)`**:
    
    - **Goal**: Verify that `send_welcome_email` handles exceptions gracefully (returns `False`).
    - **Mocking**: Specifically, the `sendmail` method on the mocked `SMTP` instance is configured to raise an `smtplib.SMTPException`.
    - **Assertion**: It checks that `send_welcome_email` returns `False` and that `sendmail` was indeed called (even though it raised an exception).

By using mocking, these tests can run quickly and reliably without any external dependencies, allowing us to focus solely on the logic within `send_welcome_email`.

### 5.3 Best Practicses for Mocking

+ **Mock at the boundary**: Mock external dependencies where your code interacts with them. 
+ **Avoid over-mocking**: Don't mock every single internal function. This makes tests brittle and less valuable. 
+ **Be explicit**: Clearly define what your mock should do. 
+ *Use `mocker` fixture: :It handles setup and teardown of patches automatically. 

## Module 6: Advanced Topics & Variations

### 6.1 `pytest.raises` - Testing Exceptions

To test if a function correctly raises an exception, use `pytest.raises` as a context manager. 

Let me show you an example now. 

```python
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
```

**How it works**

**Explanation of `test_pytest_raises.py`**

The file contains a simple function `divide` and two test functions that use `pytest.raises` to check its exception-raising behavior.

1. The `divide` function

This is the function under test. It performs division of `a` by `b`. Crucially, it includes a check: if `b` is `0`, it explicitly raises a `ValueError` with a specific message "Cannot divide by zero!". Otherwise, it returns the result of the division. Now we need to test this, which means when this function is invoked with 2 numbers, if the denominatory is zero then it should raise a `ValueError` exception with that configure message.


2. `test_divide_by_zero()`

This test case is designed to verify that the `divide` function correctly raises a `ValueError` when attempting to divide by zero.

- **`with pytest.raises(ValueError, match="Cannot divide by zero!"):`**: This is the core of the exception testing.
    - `pytest.raises` is used as a context manager.
    - The first argument, `ValueError`, tells `pytest` to expect an exception of this specific type. If any other exception type is raised, or no exception is raised at all, the test will fail.
    - The `match` argument is optional but highly recommended. It takes a regular expression string and asserts that the message of the raised exception matches this pattern. This ensures that not only the correct type of exception is raised, but also that it carries the expected message, providing more robust testing.
- **`divide(10, 0)`**: Inside the `with` block, the `divide` function is called with arguments that are expected to trigger the `ValueError` (i.e., division by zero).

This test is expected to **pass** because `divide(10, 0)` will indeed raise a `ValueError` with the message "Cannot divide by zero!", matching the expectation.

#### 3. `test_divide_by_zero_specific_type()`

This test case also attempts to divide by zero, but it expects a different type of exception: `ZeroDivisionError`.

- **`with pytest.raises(ZeroDivisionError):`**: Here, `pytest` is instructed to expect a `ZeroDivisionError`.
- **`divide(10, 0)`**: As before, this call will raise a `ValueError`.

This test is explicitly designed to **fail**. The `divide` function raises a `ValueError`, but the test is asserting that a `ZeroDivisionError` should be raised. Since the actual exception type (`ValueError`) does not match the expected exception type (`ZeroDivisionError`), `pytest` will report this test as a failure. This demonstrates the importance of specifying the correct exception type when using `pytest.raises`.

`pytest.raises` is a powerful tool for testing error conditions. When the code inside the `with` block raises the specified exception type (and optionally, a message matching the `match` regex), the test passes. If the code raises a different exception, or no exception at all, the test fails. This allows you to write precise tests for how your functions handle invalid inputs or unexpected situations.

### 6.2 `pytest.fixture` with `request` object

Fixtures can introspect the requesting test context (test function, class, module) using the `request` object. This is useful for dynamic fixture behavior.

Let me show you an example now. Below is the `conftest.py` file. 

```python
# conftest.py
import pytest

@pytest.fixture
def resource(request):
    # Get a custom marker value from the requesting test
    marker = request.node.get_closest_marker("resource_id")
    resource_id = marker.args[0] if marker and marker.args else "default_resource"
    print(f"\nSetting up resource: {resource_id}")
    yield f"Resource_{resource_id}"
    print(f"Tearing down resource: {resource_id}")

```

Below is the test file. 

```python
# test_resources.py
import pytest

@pytest.mark.resource_id("alpha")
def test_use_resource_alpha(resource):
    assert resource == "Resource_alpha"

@pytest.mark.resource_id("beta")
def test_use_resource_beta(resource):
    assert resource == "Resource_beta"

def test_use_default_resource(resource):
    assert resource == "Resource_default_resource"
```

**How it works**

**Explanation of `conftest.py`**

This file defines a `pytest` fixture named `resource` that dynamically adapts its behavior based on markers applied to the tests that use it.

**Key aspects of `conftest.py`:**

1. **`conftest.py`'s Special Role:** In `pytest`, `conftest.py` is a special file. Any fixtures defined within it are automatically discovered and made available to tests in the same directory and its subdirectories, without needing explicit imports. This promotes reusability and organization of test setup code.
2. **`@pytest.fixture` Decorator:** This decorator marks the `resource` function as a `pytest` fixture.
3. **`request` Object:** The `resource` fixture takes `request` as an argument. `request` is a built-in `pytest` fixture that provides introspection capabilities into the requesting test context (e.g., the test function, class, or module that is using the fixture).
4. **Dynamic Resource ID Retrieval:**
    - `marker = request.node.get_closest_marker("resource_id")`: This line is crucial. It uses the `request` object to look for a `pytest.mark.resource_id` marker on the test node (the test function in this case) that is currently requesting the `resource` fixture.
    - `resource_id = marker.args[0] if marker and marker.args else "default_resource"`: This extracts the value passed to the `resource_id` marker.
        - If a `resource_id` marker is found (`marker` is not `None`) and it has arguments (`marker.args` is not empty), it takes the first argument (`marker.args[0]`) as the `resource_id`.
        - If no `resource_id` marker is found, or if it's found but has no arguments, it defaults to `"default_resource"`.
5. **Setup and Teardown:**
    - `print(f"\nSetting up resource: {resource_id}")`: This line is executed during the fixture's setup phase, indicating which specific resource is being prepared.
    - `yield f"Resource_{resource_id}"`: The `yield` keyword is what makes this a "yielding fixture." The value `f"Resource_{resource_id}"` is passed to the test function that requested the fixture. The test function then executes.
    - `print(f"Tearing down resource: {resource_id}")`: After the test function completes (or fails), the code after `yield` is executed, serving as the teardown phase. This is where you'd typically clean up resources.

In essence, this `conftest.py` sets up a flexible `resource` fixture that can be configured by the individual tests that consume it, allowing for different "resources" to be provisioned based on test-specific metadata.

**Explanation of `test_resources.py`**

This file contains test functions that demonstrate how to use the `resource` fixture from `conftest.py` and how to influence its behavior using the custom `resource_id` marker.

**Key aspects of `test_resources.py`:**

1. **Import `pytest`:** Necessary for using `pytest` features like markers.
2. **`test_use_resource_alpha(resource)`:**
    - `@pytest.mark.resource_id("alpha")`: This line applies a custom marker named `resource_id` to this test function, passing `"alpha"` as its argument.
    - When `pytest` runs this test, it sees that `test_use_resource_alpha` requires the `resource` fixture.
    - The `resource` fixture (from `conftest.py`) is then invoked. Inside the fixture, `request.node.get_closest_marker("resource_id")` will find this marker, and `resource_id` will be set to `"alpha"`.
    - The fixture will yield `"Resource_alpha"`, which is then passed as the `resource` argument to the test function.
    - `assert resource == "Resource_alpha"`: This assertion verifies that the test received the expected resource value.
3. **`test_use_resource_beta(resource)`:**
    - This test functions identically to `test_use_resource_alpha`, but it uses `@pytest.mark.resource_id("beta")`.
    - Consequently, the `resource` fixture will yield `"Resource_beta"`, and the assertion verifies this.
4. **`test_use_default_resource(resource)`:**
    - This test function also requests the `resource` fixture, but it **does not** have a `pytest.mark.resource_id` marker applied to it.
    - When the `resource` fixture is invoked for this test, `request.node.get_closest_marker("resource_id")` will return `None`.
    - As per the logic in `conftest.py`, `resource_id` will then default to `"default_resource"`.
    - The fixture will yield `"Resource_default_resource"`, and the assertion verifies this.

**How They Work Together**

These two files demonstrate a powerful `pytest` pattern:

- **Dynamic Fixture Configuration:** The `resource` fixture in `conftest.py` is designed to be flexible. Instead of being hardcoded, it uses the `request` object to inspect the test that is calling it.
- **Test-Specific Resource Provisioning:** By applying different `pytest.mark.resource_id` markers to individual test functions in `test_resources.py`, each test can effectively "tell" the `resource` fixture what kind of resource it needs. This allows for a single fixture definition to serve multiple test scenarios, reducing code duplication and making tests more readable and maintainable.
- **Clear Separation of Concerns:** The fixture defines _how_ a resource is set up and torn down, while the tests define _what_ resource they need for their specific logic.

When you run `pytest` in the directory containing these files, you would see output similar to this (order might vary slightly depending on `pytest` version and execution environment):

(Note: The "Tearing down resource" messages would appear after each test completes, but `pytest` often buffers output, so they might appear together at the end or interleaved depending on verbosity settings.)

This setup is incredibly useful for scenarios like:

- Connecting to different database instances (e.g., `test_db_alpha`, `test_db_beta`).
- Configuring different API clients.
- Setting up different test environments or user roles.

#### 6.2.1 Use Cases for `pytest.fixture` with `request` objects

##### 6.2.1.1 Setting up different user roles


1.  `conftest.py`

This file defines a `pytest` fixture named `user_session`. In `pytest`, the `conftest.py` files are special because any fixtures defined within them are automatically discovered and made available to tests in the same directory and its subdirectories, without needing explicit imports.

**Key aspects of this `conftest.py`:**

- **`@pytest.fixture`**: This decorator marks `user_session` as a `pytest` fixture.
- **`request` object**: The fixture takes `request` as an argument. This is a built-in `pytest` fixture that provides introspection into the test context that is requesting the fixture.
- **Dynamic Role Determination**:
    - `marker = request.node.get_closest_marker("user_role")`: This line is crucial. It uses the `request` object to look for a custom `pytest.mark.user_role` marker on the test function that is currently using this fixture.
    - `role = marker.args[0] if marker and marker.args else "guest"`: If the `user_role` marker is found and has an argument (e.g., `@pytest.mark.user_role("admin")`), it extracts that argument (`"admin"`) as the `role`. If no such marker is found, or if it has no arguments, it defaults the `role` to `"guest"`.
- **Setup and Teardown**:
    - `print(f"\n--- Setting up session for user role: {role} ---")`: This code runs _before_ the test, simulating the setup phase (e.g., logging in a user with a specific role).
    - `yield session`: The `yield` keyword makes this a "yielding fixture." The `session` dictionary (e.g., `{"user": "user_admin", "role": "admin"}`) is passed to the test function that requested the fixture. The test function then executes.
    - `print(f"--- Tearing down session for user role: {role} ---")`: This code runs _after_ the test completes (or fails), simulating the teardown phase (e.g., logging out or cleaning up the session).

In essence, this `conftest.py` defines a flexible `user_session` fixture that can be configured by individual tests to provide different user roles.

2. `test_roles.py`

This file contains the test functions that consume the `user_session` fixture and demonstrate how to influence its behavior using the custom `user_role` marker.


**Key aspects of this `test_roles.py`:**

- **Requesting the Fixture**: Each test function (`test_admin_dashboard_access`, `test_editor_content_creation`, `test_guest_browsing`) includes `user_session` as an argument in its signature. This tells `pytest` that these tests depend on the `user_session` fixture.
- **Using `pytest.mark.user_role()`**:
    - `@pytest.mark.user_role("admin")`: This marker is applied to `test_admin_dashboard_access`. When `pytest` runs this test, the `user_session` fixture will detect this marker and set the `role` to `"admin"`. The fixture will then yield a session like `{"user": "user_admin", "role": "admin"}`.
    - `@pytest.mark.user_role("editor")`: Similarly, for `test_editor_content_creation`, the `role` will be set to `"editor"`.
- **Default Behavior**: `test_guest_browsing` does _not_ have a `pytest.mark.user_role` marker. When the `user_session` fixture is invoked for this test, it won't find the marker and will fall back to its default `role` of `"guest"`.

###### How They Work Together

These two files demonstrate a powerful `pytest` pattern for managing test setup:

1. **Dynamic Fixture Configuration**: The `user_session` fixture in `conftest.py` is designed to be flexible. Instead of being hardcoded to a single role, it uses the `request` object to inspect the test that is calling it.
2. **Test-Specific Setup**: By applying different `pytest.mark.user_role` markers to individual test functions in `test_roles.py`, each test can effectively "tell" the `user_session` fixture what kind of user session it needs. This allows for a single fixture definition to serve multiple test scenarios (admin, editor, guest), reducing code duplication and making tests more readable and maintainable.
3. **Clear Separation of Concerns**:
    - The `conftest.py` (fixture) defines _how_ a user session is set up and torn down (e.g., the logic for creating a session based on a role).
    - The `test_roles.py` (tests) defines _what_ specific user role they need for their particular test logic.

When you run `pytest` in this directory, for each test function, `pytest` will:

1. Identify that the test needs the `user_session` fixture.
2. Call the `user_session` fixture.
3. Inside the fixture, `request.node.get_closest_marker("user_role")` will check the current test function for the `user_role` marker.
4. Based on the marker (or its absence), the fixture will configure and yield the appropriate `user_session` dictionary.
5. The test function then executes with that specific `user_session`.
6. After the test completes, the teardown code in the fixture runs.

This setup is incredibly useful for testing features that behave differently based on user permissions or roles, allowing you to write concise and targeted tests.

**Note on `pytest.ini`**: For `pytest` to recognize custom markers like `user_role` without warnings, it's good practice to register them in a `pytest.ini` file at the root of your project:

This ensures `pytest` knows about your custom marker and can provide better reporting and validation.

##### 6.2.1.2 Setting up different DB instances


1. `conftest.py`

This file defines a `pytest` fixture named `db_connection`. Its purpose is to provide a "database connection" object to tests, where the type of database can be specified by the test itself.

**Key aspects of this `conftest.py`:**

- **`@pytest.fixture`**: Marks `db_connection` as a fixture, making it available to tests in the same directory.
- **`request` object**: The fixture uses the built-in `request` object to inspect the test function that is asking for this fixture.
- **Dynamic Database Type**:
    - `marker = request.node.get_closest_marker("db_type")`: This is the core of the dynamic behavior. It looks for a `@pytest.mark.db_type(...)` marker on the test function.
    - `db_type = marker.args[0] if marker and marker.args else "sqlite"`: This line checks if a `db_type` marker was found. If it was, it uses the first argument passed to the marker (e.g., `"postgresql"`) as the `db_type`. If no marker is found, it falls back to a default value of `"sqlite"`.
- **Setup/Teardown Simulation**:
    - The code before `yield` simulates setting up a connection to the determined database type.
    - `yield conn`: This provides the simulated connection string (e.g., `"Connection_to_Postgresql_DB"`) to the test function.
    - The code after `yield` simulates tearing down the connection after the test has finished.

2. `test_database.py`

This file contains the tests that consume the `db_connection` fixture. Each test uses a specific marker (or no marker) to get the exact type of database connection it needs.


**Key aspects of this `test_database.py`:**

- **`test_read_from_postgresql(db_connection)`**:
    - This test requests the `db_connection` fixture.
    - It is decorated with `@pytest.mark.db_type("postgresql")`.
    - The `db_connection` fixture sees this marker and sets `db_type` to `"postgresql"`, yielding the value `"Connection_to_Postgresql_DB"`.
    - The `assert` statement confirms that the correct connection object was received.
- **`test_write_to_mysql(db_connection)`**:
    - This test also requests the `db_connection` fixture.
    - It is decorated with `@pytest.mark.db_type("mysql")`.
    - The fixture sets `db_type` to `"mysql"` and yields `"Connection_to_Mysql_DB"`.
    - The assertion verifies this.
- **`test_default_db_operation(db_connection)`**:
    - This test requests the fixture but has **no `db_type` marker**.
    - The `db_connection` fixture does not find a marker and uses its default value, setting `db_type` to `"sqlite"`.
    - It yields `"Connection_to_Sqlite_DB"`, which the test then asserts.

**How They Work Together**

The interaction between these two files is a perfect illustration of separating the "how" from the "what" in testing:

1. **The Fixture `conftest.py` defines _how_ to create a resource.** It contains the logic to set up and tear down a database connection and is flexible enough to handle different types.
2. **The Tests `test_database.py` define _what_ resource they need.** Each test uses a marker to declare its specific requirement (a PostgreSQL connection, a MySQL connection, or the default SQLite connection).

When you run `pytest`, it orchestrates this interaction for each test:

- For `test_read_from_postgresql`, `pytest` sees the `db_type` marker, tells the `db_connection` fixture to use "postgresql", and injects the resulting connection object into the test.
- It does the same for `test_write_to_mysql` with the "mysql" marker.
- For `test_default_db_operation`, it sees no marker, so the fixture provides the default "sqlite" connection.

This pattern makes your test suite highly maintainable and readable. If you need to add tests for a new database (e.g., Oracle), you don't need to change the fixture's logic; you simply add a new test with `@pytest.mark.db_type("oracle")`.

### 6.4 `pytest.main()` - Programmatic Test Execution

We can run `pytest` programmatically from your python code. This is usefull for integrating with other tools or custom test runners. 

```python
import pytest

# In a separate script, e.g., run_tests.py
if __name__ == "__main__":
    # Run all tests in the current directory
    pytest.main()

    # Run specific tests with options
    # pytest.main(['-v', 'test_calculator.py::test_add_positive_numbers'])
```

### 6.5 Plugins

`pytest` has an extensive plugin ecosystem. Most popular ones are:

+ `pytest-cov`: for code coverage reports ( `pip install pytest-cov`, `pytest --cov=module_name`)
+ `pytest-xdist`: Parallel test execusion ( `pip install pytest-xdist`)
, `pytest -n auto`)
+ `pytest-html`: Generate HTML reports
+ `pytest-bdd`: For behavior driven development (BDD) testing
+ `pytest-asyncio`: For testing asynchronous code
+ `pytest-sugar`: For prettier and more informative test output. 

### 6.6 Best Practices for Writing Effective Tests

+ Follow the AAA Pattern:

    + Arrange: Setup the test data and environment
    + Act: Perform the action you want to test
    + Assert: Verify the expected result

+ Keep Tests Simple and Focused: Each test should ideally test one specific piece of functionality. 
+ Meaningful Test Names: Use descriptive names that clearly indicate what the test is testing. 
+ Test Isolation: Tests should be independent of each other. Fixtures help achieve this. 
+ Run Tests Frequently: 
+ Structure your Tests: Organize your test files and directories mirroring your application's structure. Often, a tests/ directory at the project root is a good approach. 

```
    my_project/
    ├── src/
    │   └── my_app/
    │       ├── __init__.py
    │       └── module_a.py
    │       └── module_b.py
    └── tests/
        ├── __init__.py
        ├── conftest.py
        ├── unit/
        │   ├── test_module_a.py
        │   └── test_module_b.py
        └── integration/
            └── test_api_integration.py
```






