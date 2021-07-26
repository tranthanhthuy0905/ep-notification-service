from django.db import models

class SlackModel(models.Model):
    slackURl = models.URLField(blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TeamsModel(models.Model):
    message = models.TextField(blank=False, null=False)
    teamsURl = models.URLField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OutlookModel(models.Model):
    subject = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(blank=False, null=False)
    recipient = models.CharField(max_length=200, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TelegramModel(models.Model):
    message = models.TextField(blank=False, null=False)
    telegramURl = models.URLField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
