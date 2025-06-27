# conftest.py
import pytest

@pytest.fixture(params=["chrome", "firefox"], ids=["browser_chrome", "browser_firefox"])
def browser(request): # request is a special fixture
    """Provides different browser instances."""
    browser_name = request.param
    print(f"\nSetting up {browser_name} browser")
    yield f"Browser_Object_{browser_name}"
    print(f"Closing {browser_name} browser")
