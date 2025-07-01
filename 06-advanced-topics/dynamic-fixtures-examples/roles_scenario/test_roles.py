import pytest

@pytest.mark.user_role("admin")
def test_admin_dashboard_access(user_session):
    """
    Tests admin dashboard access using an admin user session.
    """
    print(f"Test: Accessing dashboard as {user_session['user']} ({user_session['role']})")
    assert user_session["role"] == "admin"

@pytest.mark.user_role("editor")
def test_editor_content_creation(user_session):
    """
    Tests content creation using an editor user session.
    """
    print(f"Test: Creating content as {user_session['user']} ({user_session['role']})")
    assert user_session["role"] == "editor"

def test_guest_browsing(user_session):
    """
    Tests browsing functionality using a guest user session.
    """
    print(f"Test: Browsing as {user_session['user']} ({user_session['role']})")
    assert user_session["role"] == "guest"