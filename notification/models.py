from django.db import models

class NotificationModel(models.Model):
    message = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class SlackModel(NotificationModel):
    url = models.URLField(max_length=250, blank=False, null=False)

class TeamsModel(NotificationModel):
    url = models.URLField(max_length=250, blank=False, null=False)

class TelegramModel(NotificationModel):
    telegram_token = models.CharField(max_length=100, blank=False, null=False)
    telegram_chatID= models.CharField(max_length=20, blank=False, null=False)

class OutlookModel(NotificationModel):
    subject = models.CharField(max_length=100, null=False, blank=False)
    recipient = models.CharField(max_length=200, blank=False, null=False)
