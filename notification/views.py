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
import json
import logging
import traceback

logger = logging.getLogger(__name__)

class SlackView(APIView):
    @swagger_auto_schema(request_body=SlackSerializers)
    def post(self, request):
        url = request.data.get('url')
        message =request.data.get('message')
        saved_message = SlackModel(url=url, message=message)
        saved_message.save()
        post_data = {
            "text": message,
        }
        if url == "":
            return Response(
                    {"message": "Sorry! The service failed to send notification to Slack with no URL Webhook"},
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            response = requests.post(url, json.dumps(post_data))
            if response.text=="ok":
                return Response(
                    {"message": "Successfully send notification to Slack"},
                    status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {"message": "Sorry! The service failed to send notification to Slack"},
                    status=status.HTTP_400_BAD_REQUEST)



class TeamsView(APIView):
    @swagger_auto_schema(request_body=TeamsSerializers)
    def post(self, request):
        url = request.data.get('url')
        message =request.data.get('message')
        saved_message = TeamsModel(url=url, message=message)
        saved_message.save()
        post_data = {
            "text": message,
        }
        if url == "":
            return Response(
                    {"message": "Sorry! The service failed to send notification to Microsoft Teams with no URL Webhook"},
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            response = requests.post(url, json.dumps(post_data))
            if response.text=="1":
                return Response(
                    {"message": "Successfully send notification to Microsoft Teams"},
                    status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {"message": "Sorry! The service failed to send notification to Microsoft Teams"},
                    status=status.HTTP_400_BAD_REQUEST)


class OutlookView(APIView):
    @swagger_auto_schema(request_body=OutlookSerializers)
    def post(self, request):
        subject = request.data.get('subject')
        message = request.data.get('message')
        recipient = request.data.get('recipient')
        saved_message = OutlookModel(subject=subject, message=message, recipient=recipient)
        saved_message.save()

        try:
            send_mail(subject,
                      message,
                      Common.EMAIL_HOST_USER, [recipient])
            return Response(
                {"message": "Successfully send notification to " + recipient},
                status=status.HTTP_201_CREATED)
        except:
            traceback.print_exc()
            return Response(
                {
                    "message":
                    "Sorry! The service failed to send notification to " + recipient
                },
                status=status.HTTP_400_BAD_REQUEST)

class TelegramView(APIView):
    @swagger_auto_schema(request_body=TelegramSerializers)
    def post(self, request):
        telegram_token = request.data.get('telegram_token')
        telegram_chatID = request.data.get('telegram_chatID')
        message = request.data.get('message')
        saved_message = TelegramModel(telegram_token=telegram_token, telegram_chatID = telegram_chatID, message=message)
        saved_message.save()

        url = 'https://api.telegram.org/bot' + telegram_token+ '/sendMessage?chat_id=' + telegram_chatID + '&text="' + message + '"'

        response = requests.get(url)
        if response.status_code == 200:
            return Response(
                {"message": "Successfully send notification to Telegram"},
                status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "Sorry! The service failed to send notification to Telegram"},
                status=status.HTTP_400_BAD_REQUEST)

        