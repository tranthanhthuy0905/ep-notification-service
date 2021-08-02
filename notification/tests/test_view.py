from .BaseTest import BaseTest
from rest_framework import status
from notification.models import SlackModel, TeamsModel, TelegramModel, OutlookModel
from django.core.mail import send_mail
from ep_notification_service.config.common import Common
import logging
logger = logging.getLogger(__name__)

class TestViews(BaseTest):

    def post_cases(self, service, model, url, webhook, status):
        initialAmount = model.objects.count()
        data = {'url': webhook,
            'message' :'This works for testing purpose'}
        response = self.client.post(url, data, format = 'json')

        if webhook == "":
            self.assertEqual(response.status_code, status,
                    "Should FAIL to push notification to " + service + " without URL Webhook or destination contact point.")
            self.assertEqual(model.objects.get().url, '',
                    "Should store the empty url once sending notification to " + service + " with no URL Webhook input.")
        else:
            self.assertEqual(response.status_code, status,
                        "Should SUCCEED to push notification to " + service + " with correct URL Webhook or destination contact point.")
            self.assertEqual(model.objects.count(), initialAmount + 1,
                        "Should SUCCEED to update notification data to " + service + "'s database.")
            self.assertEqual(model.objects.get().message, 'This works for testing purpose')

    def post_telegram_cases(self, url, telegram_token, telegram_chatID, status):
        initialAmount = TelegramModel.objects.count()
        data = { 'telegram_token': telegram_token,
                'telegram_chatID': telegram_chatID,
                'message': 'This works for testing purpose'}
        response = self.client.post(url, data, format = 'json')

        if telegram_token == "" and telegram_chatID == "":
            self.assertEqual(response.status_code, status,
                    "Should FAIL to push notification to Telegrams without chat bot token and id.")
            self.assertTrue(TelegramModel.objects.get().telegram_token == '' and TelegramModel.objects.get().telegram_chatID == '',
                    "Should store the empty telegram information once sending notification to Telegram with no chat token and id.")
        elif telegram_token == "":
            self.assertEqual(response.status_code, status,
                    "Should FAIL to push notification to Telegrams without chat bot token.")
            self.assertEqual(TelegramModel.objects.get().telegram_token, '',
                    "Should store the empty telegram token once sending notification to Telegram without it.")
        elif telegram_chatID == "":
            self.assertEqual(response.status_code, status,
                    "Should FAIL to push notification to Telegrams without chat id.")
            self.assertEqual(TelegramModel.objects.get().telegram_chatID, '',
                    "Should store the empty telegram chat ID once sending notification to Telegram without it.")
        else:
            self.assertEqual(response.status_code, status,
                        "Should SUCCEED to push notification to Telegram with correct chat bot token and id.")
            self.assertEqual(TelegramModel.objects.count(), initialAmount + 1,
                        "Should SUCCEED to update notification data to Telegram's database with correct chat bot token and id.")
            self.assertEqual(TelegramModel.objects.get().message, 'This works for testing purpose')

    def send_mail_cases(self, subject, recipient):
        initialAmount = OutlookModel.objects.count()
        message = 'This works for testing purpose'
        response = send_mail(subject,
                    message,
                    Common.EMAIL_HOST_USER, [recipient])
        if recipient == '':
            self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
            self.assertTrue(OutlookModel.objects.count(), initialAmount)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(OutlookModel.objects.count(), initialAmount + 1)
        self.assertEqual(OutlookModel.objects.get().message, 'This works for testing purpose')

    def test_post_slack_full(self):
        webhook = 'https://hooks.slack.com/services/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'
        self.post_cases("Slack", SlackModel, self.slack_url, webhook, status.HTTP_201_CREATED)
    
    def test_post_slack_no_urlWebhook(self):
        self.post_cases("Slack", SlackModel, self.slack_url, "", status.HTTP_400_BAD_REQUEST)
    
    def test_post_teams_full(self):
        webhook = 'https://fuveduvn.webhook.office.com/webhookb2/f356f0c5-1600-43de-b87f-f43f4e6daa82@ee63425f-af72-4a58-82e7-e451cc92646a/IncomingWebhook/0affe314d3da4e96921ee6c0f8942b23/482048a5-a118-4079-b848-480e2505da28'
        self.post_cases("Teams", TeamsModel, self.teams_url, webhook, status.HTTP_201_CREATED)
    
    def test_post_teams_no_urlWebhook(self):
        self.post_cases("Teams", TeamsModel, self.teams_url, "", status.HTTP_400_BAD_REQUEST)

    def test_post_telegram_full(self): 
        telegram_token = '1909979117:AAE_RNiG-rV0nQV45B7aTK5YMtzd7FMbPf8'
        telegram_chatID = '1933919258'
        self.post_telegram_cases(self.telegram_url, telegram_token, telegram_chatID,  status.HTTP_200_OK)

    def test_post_telegram_no_chatToken(self):
        telegram_chatID = '1933919258'
        self.post_telegram_cases(self.telegram_url, "", telegram_chatID, status.HTTP_400_BAD_REQUEST)

    def test_post_telegram_no_chatId(self):
        telegram_token = '1909979117:AAE_RNiG-rV0nQV45B7aTK5YMtzd7FMbPf8'
        self.post_telegram_cases(self.telegram_url, telegram_token, "",  status.HTTP_400_BAD_REQUEST)

    def test_post_telegram_no_chatInfo(self):
        self.post_telegram_cases(self.telegram_url, "", "", status.HTTP_400_BAD_REQUEST)

    def test_post_outlook_with_recipient(self):
        self.send_mail_cases("Testing Case 01", "thuy.tran.200097@student.fulbright.edu.vn")
    
    def test_post_outlook_without_recipient(self):
        self.send_mail_cases("Testing Case 01", "") 

    def test_post_outlook_without_subject(self):
        self.send_mail_cases("", "thuy.tran.200097@student.fulbright.edu.vn")