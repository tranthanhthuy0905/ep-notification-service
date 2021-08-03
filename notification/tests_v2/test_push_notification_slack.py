import pytest
from notification.tests_v2.fixtures import slack_url, slack_url_webhook, message


@pytest.mark.django_db
def test_post_slack_full(client, slack_url_webhook, slack_url, message):
    post_data = {
        'url': slack_url_webhook,
        'message': message
    }
    response = client.post(slack_url, post_data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_push_slack_null_url(client, slack_url_webhook, slack_url, message):
    post_data = {
        'url': "",
        'message': message
    }
    response = client.post(slack_url, post_data)
    assert response.status_code == 400
