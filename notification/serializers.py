from rest_framework import serializers
from .models import SlackModels, TeamsModels, TelegramModels, OutlookModels

class SlackSerializers(serializers.ModelSerializer):
    class Meta:
        model = SlackModels
        fields = '__all__'

class TeamsSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeamsModels
        fields = '__all__'

class OutlookSerializers(serializers.ModelSerializer):
    class Meta:
        model = OutlookModels
        fields = '__all__'

class TelegramSerializers(serializers.ModelSerializer):
    class Meta:
        model = SlackModels
        fields = '__all__'