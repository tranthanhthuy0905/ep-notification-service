#from rest_framework.viewsets import ViewSet
import requests
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .models import SlackModel, TeamsModel, TelegramModel, OutlookModel
from .serializers import SlackSerializers, TeamsSerializers, TelegramSerializers, OutlookSerializers
from ep_notification_service.config.common import Common
import traceback
from rest_framework.parsers import JSONParser
import json

class SlackView(APIView):
    @swagger_auto_schema(request_body=SlackSerializers)
    def post(self, request):

        url = Common.SLACK_URL_WEBHOOK
        message =request.data.get('message')
        saved_message = SlackModel(slackURl=url, message=message)
        saved_message.save()
        
        data = JSONParser().parse(request)
        serializer = SlackSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            response = requests.post(url)
            return Response({"message": response.text},
                            status=response.status_code)
        traceback.print_exc()
        return Response(
                {
                    "message":
                    "Sorry! The service failed to send notification to Slack"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class SlackView(ViewSet):
#     queryset = SlackModel.objects.all()
#     serializer = SlackSerializers

# class TeamsView(ViewSet):
#     queryset = TeamsModel.objects.all()
#     serializer = TeamsSerializers

# class OutlookView(ViewSet):
#     queryset = OutlookModel.objects.all()
#     serializer = OutlookSerializers

# class TelegramView(ViewSet):
#     queryset = TelegramModel.objects.all()
#     serializer = TelegramSerializers