import pytest
from django.urls import reverse
from ep_notification_service.config.common import Common


@pytest.fixture(scope='function')
def teams_url():
    return reverse('teams')


@pytest.fixture(scope='function')
def teams_url_webhook():
    return Common.TEAMS_URL_WEBHOOK
