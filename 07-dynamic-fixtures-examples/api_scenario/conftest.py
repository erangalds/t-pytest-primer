import pytest

@pytest.fixture
def api_client(request):
    """
    Fixture to simulate an API client for different versions.
    The API version (e.g., v1, v2, v3) is determined by the 'api_version'
    marker on the requesting test.
    """
    marker = request.node.get_closest_marker("api_version")
    # Default to 'v1' if no marker or argument is provided
    version = marker.args[0] if marker and marker.args else "v1"

    print(f"\n--- Initializing API client for version {version} ---")
    # In a real scenario, you would instantiate an API client for the given version
    client = f"ApiClient_{version.upper()}"
    yield client  # Provide the API client object to the test
    print(f"--- Tearing down API client for version {version} ---")