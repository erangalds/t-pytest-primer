import pytest 

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