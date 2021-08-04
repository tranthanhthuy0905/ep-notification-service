import pytest
from .fixtures.slack import slack_url, slack_url_webhook
from .fixtures.message import message


@pytest.mark.django_db
def test_post_slack_full(client, slack_url_webhook, slack_url, message):
    post_data = {
        'url': slack_url_webhook,
        'message': message
    }
    response = client.post(slack_url, post_data)
    result = response.json()
    assert response.status_code == 201
    assert result.get("message") == "Successfully send notification to Slack"


@pytest.mark.django_db
def test_push_slack_null_url(client, slack_url_webhook, slack_url, message):
    post_data = {
        'url': "",
        'message': message
    }
    response = client.post(slack_url, post_data)
    result = response.json()
    assert response.status_code == 400
    assert result.get('message') == 'Sorry! The service failed to send notification to Slack with no URL Webhook'
