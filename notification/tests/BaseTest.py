from rest_framework import APITestCase
from django.urls import reverse

class BaseTest(APITestCase):
    def setUp(self):
        self.epns_url = reverse('epns')
        self.slack_url = reverse('slack')
        self.outlook_url = reverse('outlook')
        self.teams_url = reverse('teams')
        self.telegram_url = reverse('telegram')
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
