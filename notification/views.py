import requests
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .models import SlackModel, TeamsModel, TelegramModel, OutlookModel
from .serializers import SlackSerializers, TeamsSerializers, TelegramSerializers, OutlookSerializers
from ep_notification_service.config.common import Common
from notification.utils import errors, success
import json
import logging
import traceback

logger = logging.getLogger(__name__)


class SlackView(APIView):
    @swagger_auto_schema(request_body=SlackSerializers)
    def post(self, request):
        url = request.data.get('url')
        message = request.data.get('message')
        saved_message = SlackModel(url=url, message=message)
        saved_message.save()
        post_data = message.replace("\'", "\"")  # Convert data before send
        if url == "" or url == "string":
            error = errors.SLACK_URLWEBHOOK_ERROR
            logger.error(f"{error}")
            return Response({"message": error},
                            status=status.HTTP_404_NOT_FOUND)
        elif message == "" or message == "string":
            error = errors.MESSAGE_ERROR
            logger.error(f"{error}")
            return Response({"message": error},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            headers = {'Content-Type': "application/json"}
            response = requests.post(url, post_data, headers=headers)
            if response.status_code == 200:
                return Response(
                    {"message": success.SLACK_NOTIFICATION_SUCCESS},
                    status=status.HTTP_201_CREATED)
            else:
                error_text = response.text
                logger.error(
                    f"{error_text}, status code: {response.status_code}")
                return Response({"message": error_text},
                                status=response.status_code)


class TeamsView(APIView):
    @swagger_auto_schema(request_body=TeamsSerializers)
    def post(self, request):
        url = request.data.get('url')
        message = request.data.get('message')
        saved_message = TeamsModel(url=url, message=message)
        saved_message.save()
        post_data = message.replace("\'", "\"")  # Convert data before send
        if url == "" or url == "string":
            error = errors.TEAMS_URLWEBHOOK_ERROR
            logger.error(f"{error}")
            return Response({"message": error},
                            status=status.HTTP_404_NOT_FOUND)
        elif message == "" or message == "string":
            error = errors.MESSAGE_ERROR
            logger.error(f"{error}")
            return Response({"message": error},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            headers = {'Content-Type': "application/json"}
            response = requests.post(url, post_data, headers=headers)
            if response.status_code == 200:
                return Response(
                    {"message": success.TEAMS_NOTIFICATION_SUCCESS},
                    status=status.HTTP_201_CREATED)
            else:
                error_text = response.text
                logger.error(
                    f"{error_text}, status code: {response.status_code}")
                return Response({"message": error_text},
                                status=response.status_code)


class OutlookView(APIView):
    @swagger_auto_schema(request_body=OutlookSerializers)
    def post(self, request):
        subject = request.data.get('subject')
        message = request.data.get('message')
        recipient = request.data.get('recipient')
        saved_message = OutlookModel(subject=subject,
                                     message=message,
                                     recipient=recipient)
        saved_message.save()

        try:
            response = send_mail(subject, message, Common.EMAIL_HOST_USER,
                                 [recipient])
            return Response({"message": success.OUTLOOK_NOTIFICATION_SUCCESS},
                            status=status.HTTP_201_CREATED)
        except:
            error_text = response.text
            logger.error(f"{error_text}, status code: {response.status_code}")
            return Response({"message": error_text},
                            status=status.HTTP_400_BAD_REQUEST)


class TelegramView(APIView):
    @swagger_auto_schema(request_body=TelegramSerializers)
    def post(self, request):
        telegram_token = request.data.get('telegram_token')
        telegram_chatID = request.data.get('telegram_chatID')
        message = request.data.get('message')
        saved_message = TelegramModel(telegram_token=telegram_token,
                                      telegram_chatID=telegram_chatID,
                                      message=message)
        saved_message.save()

        url = 'https://api.telegram.org/bot' + telegram_token + '/sendMessage?chat_id=' + telegram_chatID + '&text=' + message

        response = requests.get(url)
        if telegram_token == "" or telegram_chatID == "":
            error = errors.TELEGRAM_TOKEN_ID_ERROR
            logger.error(f"{error}")
            return Response({"message": error},
                            status=status.HTTP_404_NOT_FOUND)
        elif message == "" or message == "string":
            error = errors.MESSAGE_ERROR
            logger.error(f"{error}")
            return Response({"message": error},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            if response.status_code == 200:
                return Response(
                    {"message": success.TELEGRAM_NOTIFICATION_SUCCESS},
                    status=status.HTTP_201_CREATED)
            else:
                error_text = response.text
                logger.error(
                    f"{error_text}, status code: {response.status_code}")
                return Response({"message": error_text},
                                status=response.status_code)
