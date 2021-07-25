from django.db import models

class SlackModels(models.Model):
    slackURl = models.URLField(blank=False, null=False)
    message_content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
class TeamsModels(models.Model):
    teamsURl = models.URLField(blank=False, null=False)
    message_content = models.TextField(blank=False, null=False)

class OutlookModels(models.Model):
    subject = models.CharField(max_length=False, null=False, blank=False)
    message_content = models.TextField(blank=False, null=False)
    recipient = models.CharField(max_length = False, blank=False, null=False)

class TelegramModels(models.Model):
    telegram_token = models.CharField(max_length=100, null=False, blank=False)
    telegram_chatID= models.CharField(max_length=10, null=False, blank=False)
    message_content = models.TextField(blank=False, null=False)