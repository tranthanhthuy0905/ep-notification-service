import pytest
from .fixtures.telegram import telegram_token, telegram_chat_id, telegram_url
from .fixtures.message import message


@pytest.mark.django_db
def test_push_telegram_null_url(client, telegram_url, telegram_token, telegram_chat_id):
    # TODO
    pass
