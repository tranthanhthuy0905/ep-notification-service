import pytest
from django.urls import reverse


@pytest.fixture(scope='function')
def telegram_url():
    return reverse('telegram')


@pytest.fixture(scope='function')
def telegram_token():
    return "1909979117:AAE_RNiG-rV0nQV45B7aTK5YMtzd7FMbPf8"


@pytest.fixture(scope='function')
def telegram_chat_id():
    return "1933919258"
