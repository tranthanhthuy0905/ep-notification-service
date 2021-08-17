'''
    Command run test: pytest notification/tests/test_push_notification_telegram.py
'''
from notification.models import TelegramModel
import pytest
from .fixtures.telegram import telegram_token, telegram_chat_id, telegram_url
from .fixtures.message import sample_telegram_message_template
from notification.utils import errors

@pytest.mark.django_db
def test_push_telegram_full(client, telegram_url, telegram_token, telegram_chat_id, sample_telegram_message_template):
    ''' 
        TEST CASE: Send notification to Telegram channel, provided with correct chat token and chat ID
        Expected behavior: Successfully, status code = 201 (created), new notification is updated in database
    '''

    post_data = {
        'telegram_token': telegram_token,
        'telegram_chatID': telegram_chat_id,
        'message': sample_telegram_message_template
    }
    response = client.post(telegram_url, post_data)
    assert response.status_code == 201
    assert TelegramModel.objects.get().telegram_token == telegram_token
    assert TelegramModel.objects.get().telegram_chatID == telegram_chat_id

@pytest.mark.django_db
def test_push_slack_null_token(client, telegram_url, telegram_chat_id, sample_telegram_message_template):
    ''' 
        TEST CASE: Send notification to Telegram channel without chat token
        Expected behavior: Fail, status code = 404 (not found), message of error is returned correctly
    '''

    post_data = {
        'telegram_token': "",
        'telegram_chatID': telegram_chat_id,
        'message': sample_telegram_message_template
    }
    response = client.post(telegram_url, post_data)
    result = response.json()
    assert response.status_code == 404
    assert result.get('message') == errors.TELEGRAM_TOKEN_ID_ERROR

@pytest.mark.django_db
def test_push_slack_null_id(client, telegram_url, telegram_token, sample_telegram_message_template):
    ''' 
        TEST CASE: Send notification to Telegram channel without chat id
        Expected behavior: Fail, status code = 404 (not found), message of error is returned correctly
    '''

    post_data = {
        'telegram_token': telegram_token,
        'telegram_chatID': "",
        'message': sample_telegram_message_template
    }
    response = client.post(telegram_url, post_data)
    result = response.json()
    assert response.status_code == 404
    assert result.get('message') == errors.TELEGRAM_TOKEN_ID_ERROR
