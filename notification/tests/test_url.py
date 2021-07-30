from rest_framework import status
from .BaseTest import BaseTest


class TestURL(BaseTest):

    def url_base_test(self, url):
        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_epns_url(self):
        self.url_base_test(self.epns_url)

    def test_slack_url(self):
        self.url_base_test(self.slack_url)

    def test_teams_url(self):
        self.url_base_test(self.teams_url)

    def test_telegram_url(self):
        self.url_base_test(self.telegram_url)

    def test_outlook_url(self):
        self.url_base_test(self.outlook_url)

