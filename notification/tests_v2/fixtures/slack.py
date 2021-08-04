import pytest
from django.urls import reverse
from ep_notification_service.config.common import Common


@pytest.fixture(scope='function')
def slack_url():
    return reverse('slack')


@pytest.fixture(scope='function')
def slack_url_webhook():
    return Common.SLACK_URL_WEBHOOK
