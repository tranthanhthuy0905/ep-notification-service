import pytest


@pytest.fixture(scope='function')
def sample_slack_message_template():
    # Sample message template
    message = {
        "blocks": [{
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Welcome to EPNS"
            }
        }, {
            "type": "section",
            "block_id": "section567",
            "text": {
                "type":
                "mrkdwn",
                "text":
                "<https://example.com|Overlook Hotel> \n :star: \n Doors had too many axe holes, guest in room 237 was far too rowdy, whole place felt stuck in the 1920s."
            },
            "accessory": {
                "type": "image",
                "image_url":
                "https://is5-ssl.mzstatic.com/image/thumb/Purple3/v4/d3/72/5c/d3725c8f-c642-5d69-1904-aa36e4297885/source/256x256bb.jpg",
                "alt_text": "Haunted hotel image"
            }
        }, {
            "type":
            "section",
            "block_id":
            "section789",
            "fields": [{
                "type": "mrkdwn",
                "text": "*Average Rating*\n1.0"
            }]
        }]
    }

    return message


# https://docs.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-format?tabs=adaptive-md%2Cconnector-html#format-cards-with-html
@pytest.fixture(scope='function')
def sample_teams_message_template():
    message = {
        "type":
        "message",
        "attachments": [{
            "contentType": "application/vnd.microsoft.card.adaptive",
            "contentUrl": '',
            "content": {
                "$schema":
                "http://adaptivecards.io/schemas/adaptive-card.json",
                "type":
                "AdaptiveCard",
                "version":
                "1.2",
                "body": [{
                    "type":
                    "TextBlock",
                    "text":
                    " Welcome to EPNS, join [https://adaptivecards.io/samples](https://adaptivecards.io/samples)"
                }]
            }
        }]
    }
    return message


@pytest.fixture(scope='function')
def sample_telegram_message_template():
    message = "This message is working for testing EPNS - Telegram"
    return message
