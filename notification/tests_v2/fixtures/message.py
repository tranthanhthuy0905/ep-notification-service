import pytest


@pytest.fixture(scope='function')
def message():
    # Return template
    return "This works for testing purpose."


def message_testing():
    return "Testing ..."
