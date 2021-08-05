import pytest
from django.urls import reverse
from django.conf import settings


@pytest.fixture(scope='function')
def telegram_url():
    return reverse('telegram')


@pytest.fixture(scope='function')
def telegram_token():
    return settings.TELEGRAM_TOKEN


@pytest.fixture(scope='function')
def telegram_chat_id():
    return settings.TELEGRAM_CHATID
