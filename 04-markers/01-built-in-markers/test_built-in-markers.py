import pytest
import sys

def test_always_runs():
    assert True

@pytest.mark.skip(reason="This test is temporarily disabled")
def test_disabled_feature():
    assert False # This will not run

@pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
def test_linux_only_feature():
    assert True

@pytest.mark.xfail(reason="Bug #123: This feature is currently broken")
def test_buggy_feature():
    assert 1 == 2 # This test is expected to fail