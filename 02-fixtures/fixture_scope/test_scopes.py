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