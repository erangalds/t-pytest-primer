# test_web_ui.py
import pytest

pytestmark = pytest.mark.ui # Applies 'ui' marker to all tests in this module

@pytest.mark.slow # Can combine with module-level marker
class TestHomePage:
    def test_navbar_present(self):
        assert True

    def test_footer_present(self):
        assert True

@pytest.mark.database # Overrides module-level marker for this class
class TestDatabaseInteractions:
    def test_fetch_records(self):
        assert True