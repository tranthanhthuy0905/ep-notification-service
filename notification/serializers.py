from rest_framework import serializers
from .models import SlackModel, TeamsModel, TelegramModel, OutlookModel

class SlackSerializers(serializers.ModelSerializer):
    class Meta:
        model = SlackModel
        fields = ['message']

    def create(self, validated_data):
        """
        Check the valid input
        """
        return SlackModel.objects.create(**validated_data)

class TeamsSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeamsModel
        fields = ['message']

    def create(self, validated_data):
        """
        Check the valid input
        """
        return TeamsModel.objects.create(**validated_data)

class OutlookSerializers(serializers.ModelSerializer):
    class Meta:
        model = OutlookModel
        class Meta:
            model = OutlookModel
        fields = ['message', 'subject', 'recipient']

    def create(self, validated_data):
        """
        Check the valid input
        """
        return OutlookModel.objects.create(**validated_data)

class TelegramSerializers(serializers.ModelSerializer):
    class Meta:
        model = TelegramModel
        fields = ['message']

    def create(self, validated_data):
        """
        Check the valid input
        """
        return TelegramModel.objects.create(**validated_data)