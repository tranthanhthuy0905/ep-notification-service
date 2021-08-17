'''
    Command run test: pytest notification/tests/test_push_notification_teams.py
'''
import pytest
from .fixtures.teams import teams_url, teams_url_webhook
from .fixtures.message import sample_teams_message_template
from notification.models import TeamsModel
from notification.utils import errors

@pytest.mark.django_db
def test_post_teams_full(client, teams_url_webhook, teams_url, sample_teams_message_template):
    ''' 
        TEST CASE: Send notification to Microsoft Teams channel, provided with correct Webhook URL
        Expected behavior: Successfully, status code = 201 (created), new notification is updated in database
    '''

    post_data = {
        'url': teams_url_webhook,
        'message': [sample_teams_message_template]
    }
    response = client.post(teams_url, post_data)
    assert response.status_code == 201
    assert TeamsModel.objects.get().url == teams_url_webhook


@pytest.mark.django_db
def test_post_teams_null_url_webhook(client, sample_teams_message_template, teams_url):
    ''' 
        TEST CASE: Send notification to Microsoft Teams channel without Webhook URL
        Expected behavior: Fail, status code = 404 (not found), message of error is returned correctly
    '''

    post_data = {
        'url': '',
        'message': [sample_teams_message_template]
    }
    response = client.post(teams_url, post_data)
    result = response.json()
    assert response.status_code == 404
    assert result.get('message') == errors.TEAMS_URLWEBHOOK_ERROR
