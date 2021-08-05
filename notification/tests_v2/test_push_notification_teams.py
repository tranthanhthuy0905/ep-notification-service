import pytest
from .fixtures.teams import teams_url, teams_url_webhook, teams_message
from .fixtures.message import message


@pytest.mark.django_db
def test_post_teams_full(client, teams_url_webhook, teams_message, teams_url):
    # Test data is correct url and has message
    post_data = {
        'url': teams_url_webhook,
        'message': [teams_message]
    }
    response = client.post(teams_url, post_data)
    result = response.json()

    assert response.status_code == 201
    assert result.get('message') == 'Successfully send notification to Microsoft Teams'


@pytest.mark.django_db
def test_post_teams_null_url_webhook(client, teams_message, teams_url):
    # Test data is null url and has message
    post_data = {
        'url': '',
        'message': [teams_message]
    }
    response = client.post(teams_url, post_data)
    result = response.json()

    assert response.status_code == 400
    assert result.get(
        'message') == 'Sorry! The service failed to send notification to Microsoft Teams with no URL Webhook'
