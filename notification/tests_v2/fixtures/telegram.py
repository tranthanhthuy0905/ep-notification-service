import pytest
from django.urls import reverse
from ep_notification_service.config.common import Common


@pytest.fixture(scope='function')
def telegram_url():
    return reverse('telegram')


@pytest.fixture(scope='function')
def telegram_token():
    return Common.TELEGRAM_TOKEN


@pytest.fixture(scope='function')
def telegram_chat_id():
    return Common.TELEGRAM_CHATID
