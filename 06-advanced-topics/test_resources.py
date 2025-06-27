# test_resources.py
import pytest

@pytest.mark.resource_id("alpha")
def test_use_resource_alpha(resource):
    assert resource == "Resource_alpha"

@pytest.mark.resource_id("beta")
def test_use_resource_beta(resource):
    assert resource == "Resource_beta"

def test_use_default_resource(resource):
    assert resource == "Resource_default_resource"