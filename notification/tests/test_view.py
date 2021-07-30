from .BaseTest import BaseTest
from rest_framework import status
from notification.models import SlackModel, TeamsModel, TelegramModel, OutlookModel
from django.core.mail import send_mail
from ep_notification_service.config.common import Common

class TestViews(BaseTest):

    def post_cases(self, model, url, status):
        initialAmount = model.objects.count()
        data = {'message': 'This works for testing purpose'}
        response = self.client.post(url, data, format = 'json')
        
        self.assertEqual(response.status_code, status)
        self.assertEqual(model.objects.count(), initialAmount + 1)
        self.assertEqual(model.objects.get().message, 'This works for testing purpose')

    def send_mail_cases(self, subject, recipient):
        initialAmount = OutlookModel.objects.count()
        message = 'This works for testing purpose'
        send_mail(subject,
                            message,
                            Common.EMAIL_HOST_USER, [recipient])
        if recipient == '':
            self.assertEqual(status, status.HTTP_500_INTERNAL_SERVER_ERROR)
            self.assertTrue(OutlookModel.objects.count(), initialAmount)

        self.assertEqual(status, status.HTTP_201_CREATED)
        self.assertEqual(OutlookModel.objects.count(), initialAmount + 1)
        self.assertEqual(OutlookModel.objects.get().message, 'This works for testing purpose')

    def test_post_slack(self):
        self.post_cases(SlackModel, self.slack_url, status.HTTP_201_CREATED)
    
    def test_post_teams(self):
        self.post_cases(TeamsModel, self.teams_url, status.HTTP_201_CREATED)
    
    def test_post_telegram(self): 
        self.post_cases(TelegramModel, self.telegram_url, status.HTTP_200_OK)

    def test_post_outlook_with_recipient(self):
        self.send_mail_cases("Testing Case 01", "thuy.tran.200097@student.fulbright.edu.vn")
    
    def test_post_outlook_without_recipient(self):
        self.send_mail_cases("Testing Case 01", "") 

    def test_post_outlook_without_subject(self):
        self.send_mail_cases("", "thuy.tran.200097@student.fulbright.edu.vn")