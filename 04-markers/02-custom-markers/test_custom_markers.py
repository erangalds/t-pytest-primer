import pytest 

@pytest.mark.slow
def test_performance_intensive():
    # Simulate a long-running operation
    import time 
    time.sleep(5)
    assert True 

@pytest.mark.database
def test_user_creation_in_db():
    # Connect to DB and create user
    assert True 

@pytest.mark.ui 
def test_login_button_visibility():
    # Check if login button is visible
    assert True 
