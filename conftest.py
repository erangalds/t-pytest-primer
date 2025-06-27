import pytest

@pytest.fixture
def sample_data():
    """A simple list of numbers for testing."""
    return [1, 2, 3, 4, 5]

@pytest.fixture
def empty_list():
    """An empty list."""
    return []

