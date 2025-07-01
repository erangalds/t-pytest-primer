import pytest

@pytest.fixture
def db_connection(request):
    """
    Fixture to simulate a database connection.
    The type of database (e.g., postgresql, mysql, sqlite) is determined
    by the 'db_type' marker on the requesting test.
    """
    marker = request.node.get_closest_marker("db_type")
    # Default to 'sqlite' if no marker or argument is provided
    db_type = marker.args[0] if marker and marker.args else "sqlite"

    print(f"\n--- Setting up {db_type} database connection ---")
    # In a real scenario, you would establish a connection here
    conn = f"Connection_to_{db_type.capitalize()}_DB"
    yield conn  # Provide the connection object to the test
    print(f"--- Closing {db_type} database connection ---")