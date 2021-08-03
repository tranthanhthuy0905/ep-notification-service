import pytest
from notification.tests.fixtures import slack_url, slack_urlWebhook, message

@pytest.mark.django_db
def test_post_slack_full(client):
    post_data = {
        'url': slack_urlWebhook,
        'message': message
    }
    response = client.post(slack_url, post_data)
    assert response.status_code == 201

@pytest.mark.django_db
def test_post_slack_no_urlWebhook(client):
    post_data = {
        'message': message
    }
    response = client.post(slack_url, post_data)
    assert response.status_code == 400