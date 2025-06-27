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

