import pytest

@pytest.mark.db_type("postgresql")
def test_read_from_postgresql(db_connection):
    """
    Tests reading data using a PostgreSQL connection.
    """
    print(f"Test: Reading data using {db_connection}")
    assert "Postgresql" in db_connection

@pytest.mark.db_type("mysql")
def test_write_to_mysql(db_connection):
    """
    Tests writing data using a MySQL connection.
    """
    print(f"Test: Writing data using {db_connection}")
    assert "Mysql" in db_connection

def test_default_db_operation(db_connection):
    """
    Tests an operation using the default database connection (sqlite).
    """
    print(f"Test: Performing operation using {db_connection}")
    assert "Sqlite" in db_connection