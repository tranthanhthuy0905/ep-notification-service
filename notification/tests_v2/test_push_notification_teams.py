import pytest
from notification.tests_v2.fixtures import teams_url, teams_url_webhook, message


@pytest.mark.django_db
def test_post_teams_full(client, teams_url_webhook, message, teams_url):
    # Test data is correct url and has message
    post_data = {
        'url': teams_url_webhook,
        'message': message
    }
    response = client.post(teams_url, post_data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_post_teams_null_url_webhook(client, message, teams_url):
    # Test data is null url and has message
    post_data = {
        'url': '',
        'message': message
    }
    response = client.post(teams_url, post_data)
    assert response.status_code == 400
