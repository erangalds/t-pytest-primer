# conftest.py
import pytest

@pytest.fixture(params=[10, 20], ids=["size_10", "size_20"])
def dataset_size(request):
    return request.param