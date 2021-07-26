from django.contrib import admin
from .models import SlackModel, TeamsModel, TelegramModel, OutlookModel
# Register your models here.
admin.site.register(SlackModel)
admin.site.register(TeamsModel)
admin.site.register(TelegramModel)
admin.site.register(OutlookModel)