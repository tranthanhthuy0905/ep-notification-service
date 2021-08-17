import json
import pytest
from django.urls import reverse
from django.conf import settings


@pytest.fixture(scope='function')
def teams_url():
    return reverse('teams')

@pytest.fixture(scope='function')
def teams_url_webhook():
    # Fake data
    return "https://fuveduvn.webhook.office.com/webhookb2/f356f0c5-1600-43de-b87f-f43f4e6daa82@ee63425f-af72-4a58-82e7-e451cc92646a/IncomingWebhook/0affe314d3da4e96921ee6c0f8942b23/482048a5-a118-4079-b848-480e2505da28"
