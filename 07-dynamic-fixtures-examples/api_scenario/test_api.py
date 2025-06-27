import pytest

@pytest.mark.api_version("v2")
def test_get_users_v2(api_client):
    """
    Tests fetching users using the V2 API client.
    """
    print(f"Test: Fetching users with {api_client}")
    assert "V2" in api_client

@pytest.mark.api_version("v3")
def test_create_resource_v3(api_client):
    """
    Tests creating a resource using the V3 API client.
    """
    print(f"Test: Creating resource with {api_client}")
    assert "V3" in api_client

def test_default_api_call(api_client):
    """
    Tests a default API call using the V1 API client.
    """
    print(f"Test: Making default API call with {api_client}")
    assert "V1" in api_client