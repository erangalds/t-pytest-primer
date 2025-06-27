import pytest

@pytest.fixture
def user_session(request):
    """
    Fixture to simulate a user session for different roles.
    The user role (e.g., admin, editor, guest) is determined by the 'user_role'
    marker on the requesting test.
    """
    marker = request.node.get_closest_marker("user_role")
    # Default to 'guest' if no marker or argument is provided
    role = marker.args[0] if marker and marker.args else "guest"

    print(f"\n--- Setting up session for user role: {role} ---")
    # In a real scenario, you might perform login, set up permissions, etc.
    session = {"user": f"user_{role}", "role": role}
    yield session  # Provide the session object to the test
    print(f"--- Tearing down session for user role: {role} ---")