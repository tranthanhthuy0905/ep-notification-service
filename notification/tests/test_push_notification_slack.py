'''
    Command run test: pytest notification/tests/test_push_notification_slack.py
'''
import pytest
from .fixtures.slack import slack_url, slack_url_webhook
from .fixtures.message import sample_slack_message_template
from notification.models import SlackModel
from notification.utils import errors


@pytest.mark.django_db
def test_post_slack_full(client, slack_url_webhook, slack_url,
                         sample_slack_message_template):
    ''' 
        TEST CASE: Send notification to Slack channel, provided with correct Webhook URL
        Expected behavior: Successfully, status code = 201 (created), new notification is updated in database
    '''

    post_data = {
        'url': slack_url_webhook,
        'message': [sample_slack_message_template]
    }
    response = client.post(slack_url, post_data)
    assert response.status_code == 201
    assert SlackModel.objects.get().url == slack_url_webhook

@pytest.mark.django_db
def test_push_slack_null_url(client, slack_url, sample_slack_message_template):
    ''' 
        TEST CASE: Send notification to Slack channel without Webhook URL
        Expected behavior: Fail, status code = 404 (not found), message of error is returned correctly
    '''

    post_data = {"url": "", "message": [sample_slack_message_template]}
    response = client.post(slack_url, post_data)
    result = response.json()
    assert response.status_code == 404
    assert result.get('message') == errors.SLACK_URLWEBHOOK_ERROR
