import pytest
from django.urls import reverse


@pytest.fixture(scope='function')
def slack_url():
    return reverse('slack')


@pytest.fixture(scope='function')
def slack_url_webhook():
    return "https://hooks.slack.com/services/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"
