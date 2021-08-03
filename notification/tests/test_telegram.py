import pytest
from notification.tests.fixtures import telegram_url, telegram_token, telegram_chatID, message

@pytest.mark.django_db
def test_post_telegram_full(client):
    post_data = {
        'telegram_token': telegram_token,
        'telegram_chatID': telegram_chatID,
        'message': message
    }
    response = client.post(telegram_url, post_data)
    assert response.status_code == 201

@pytest.mark.django_db
def test_post_telegram_no_token(client):
    post_data = {
        'telegram_chatID': telegram_chatID,
        'message': message
    }
    response = client.post(telegram_url, post_data)
    assert response.status_code == 400

@pytest.mark.django_db
def test_post_telegram_no_chatID(client):
    post_data = {
        'telegram_token': telegram_token,
        'message': message
    }
    response = client.post(telegram_url, post_data)
    assert response.status_code == 400

@pytest.mark.django_db
def test_post_telegram_nothing(client):
    post_data = {
        'message': message
    }
    response = client.post(telegram_url, post_data)
    assert response.status_code == 400