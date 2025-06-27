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
