from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

class BaseTest(APITestCase):
    def setUp(self):
        self.epns_url = reverse('epns')
        self.slack_url = reverse('slack')
        self.outlook_url = reverse('outlook')
        self.teams_url = reverse('teams')
        self.telegram_url = reverse('telegram')
        self.client = APIClient()
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
