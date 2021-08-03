'''File contains all the dummy data relating to the test '''

import pytest
from django.urls import reverse

@pytest.fixture(scope='function')
def slack_url():
    return  reverse('slack')

@pytest.fixture(scope='function')
def teams_url():
    return  reverse('teams')

@pytest.fixture(scope='function')
def telegram_url():
    return  reverse('telegram')

@pytest.fixture(scope='function')
def outlook_url():
    return  reverse('outlook')

@pytest.fixture(scope='function')
def slack_urlWebhook():
    return 'https://hooks.slack.com/services/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'

@pytest.fixture(scope='function')
def teams_urlWebhook():
    return 'https://fuveduvn.webhook.office.com/webhookb2/f356f0c5-1600-43de-b87f-f43f4e6daa82@ee63425f-af72-4a58-82e7-e451cc92646a/IncomingWebhook/0affe314d3da4e96921ee6c0f8942b23/482048a5-a118-4079-b848-480e2505da28'

@pytest.fixture(scope='function')
def telegram_token():
    return '1909979117:AAE_RNiG-rV0nQV45B7aTK5YMtzd7FMbPf8'

@pytest.fixture(scope='function')
def telegram_chatID():
    return '1933919258'

@pytest.fixture(scope='function')
def outlook_subject():
    return "Testing email"

@pytest.fixture(scope='function')
def outlook_recipient():
    return "thuy.tran.200097@student.fulbright.edu.vn"

@pytest.fixture(scope='function')
def message():
    # Return template
    return "This works for testing purpose."