from rest_framework import serializers
from .models import SlackModel, TeamsModel, TelegramModel, OutlookModel

class SlackSerializers(serializers.ModelSerializer):
    class Meta:
        model = SlackModel
        fields = '__all__'

    def create(self, validated_data):
        """
        Check the valid input
        """
        return SlackModel.objects.create(**validated_data)

class TeamsSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeamsModel
        fields = '__all__'

class OutlookSerializers(serializers.ModelSerializer):
    class Meta:
        model = OutlookModel
        fields = '__all__'

class TelegramSerializers(serializers.ModelSerializer):
    class Meta:
        model = TelegramModel
        fields = '__all__'