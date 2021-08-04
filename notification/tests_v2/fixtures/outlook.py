import pytest
from django.urls import reverse
from ep_notification_service.config.common import Common


@pytest.fixture(scope='function')
def outlook_url():
    return reverse('outlook')


@pytest.fixture(scope='function')
def outlook_subject():
    return "Testing email"


@pytest.fixture(scope='function')
def outlook_recipient():
    return Common.EMAIL_HOST_USER
