""" File contains all the dummy data relating to the test """

import pytest
from django.urls import reverse
from ep_notification_service.config.common import Common


@pytest.fixture(scope='function')
def slack_url():
    return reverse('slack')


@pytest.fixture(scope='function')
def teams_url():
    return reverse('teams')


@pytest.fixture(scope='function')
def telegram_url():
    return reverse('telegram')


@pytest.fixture(scope='function')
def outlook_url():
    return reverse('outlook')


@pytest.fixture(scope='function')
def slack_url_webhook():
    return Common.SLACK_URL_WEBHOOK


@pytest.fixture(scope='function')
def teams_url_webhook():
    return Common.TEAMS_URL_WEBHOOK


@pytest.fixture(scope='function')
def telegram_token():
    return Common.TELEGRAM_TOKEN


@pytest.fixture(scope='function')
def telegram_chat_id():
    return Common.TELEGRAM_CHATID


@pytest.fixture(scope='function')
def outlook_subject():
    return "Testing email"


@pytest.fixture(scope='function')
def outlook_recipient():
    return Common.EMAIL_HOST_USER


@pytest.fixture(scope='function')
def message():
    # Return template
    return "This works for testing purpose."
