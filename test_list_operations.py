def test_list_length(sample_data):
    assert len(sample_data) == 5

def test_list_sum(sample_data):
    assert sum(sample_data) == 15

def test_empty_list_length(empty_list):
    assert len(empty_list) == 0

