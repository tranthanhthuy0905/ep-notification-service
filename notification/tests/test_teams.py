import pytest
from notification.tests.fixtures import teams_url, teams_urlWebhook, message

@pytest.mark.django_db
def test_post_teams_full(client):
    post_data = {
        'url': teams_urlWebhook,
        'message': message
    }
    response = client.post(teams_url, post_data)
    assert response.status_code == 201

@pytest.mark.django_db
def test_post_teams_no_urlWebhook(client):
    post_data = {
        'message': message
    }
    response = client.post(teams_url, post_data)
    assert response.status_code == 400