import pytest
from notification.tests_v2.fixtures import telegram_url, telegram_token, telegram_chat_id, message


@pytest.mark.django_db
def test_push_telegram_null_url(client, telegram_url, telegram_token, telegram_chat_id, message):
    # TODO
    pass
