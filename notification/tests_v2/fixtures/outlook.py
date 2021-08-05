import pytest
from django.urls import reverse
from django.conf import settings


@pytest.fixture(scope='function')
def outlook_url():
    return reverse('outlook')


@pytest.fixture(scope='function')
def outlook_subject():
    return "Testing email"


@pytest.fixture(scope='function')
def outlook_recipient():
    return settings.EMAIL_HOST_USER
