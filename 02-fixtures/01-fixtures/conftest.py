import pytest

@pytest.fixture
def sample_data():
    """A simple list of numbers for testing."""
    print("Setting up sample data fixture")
    return [1, 2, 3, 4, 5]

@pytest.fixture
def empty_list():
    """An empty list."""
    print("Setting up empty list fixture")
    return []

