from .BaseTest import BaseTest
from rest_framework import status
from notification.models import SlackModel, TeamsModel, TelegramModel, OutlookModel

class TestViews(BaseTest):

    def post_request(self, model, url):
        initialAmount = model.objects.count()
        data = {'message': 'This works for testing purpose'}
        response = self.client.post(url, data, format = 'json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(model.objects.count(), initialAmount + 1)
        self.assertEqual(model.objects.get().message, 'This works for testing purpose')

    def test_post_slack(self):
        self.post_request(SlackModel, self.slack_url)
    
    def test_post_teams(self):
        self.post_request(TeamsModel, self.teams_url)
    
    def test_post_telegram(self):
        self.post_request(TelegramModel, self.telegram_url)

    def test_post_outlook(self):
        pass