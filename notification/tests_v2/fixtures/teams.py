import json
import pytest
from django.urls import reverse
from django.conf import settings


@pytest.fixture(scope='function')
def teams_url():
    return reverse('teams')


@pytest.fixture(scope='function')
def teams_url_webhook():
    return settings.TEAMS_URL_WEBHOOK


# https://docs.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-format?tabs=adaptive-md%2Cconnector-html#format-cards-with-html
@pytest.fixture(scope='function')
def teams_message():
    message = {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "contentUrl": '',
                "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.2",
                    "body": [
                        {
                            "type": "TextBlock",
                            "text": "For Samples and Templates, see [https://adaptivecards.io/samples](https://adaptivecards.io/samples)"
                        }
                    ]
                }
            }
        ]
    }
    return message
