from django.urls import path
from .views import SlackView, OutlookView, TeamsView, TelegramView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="EP Notification Service",
        default_version='v1',
        description="EP Notification Service",
        terms_of_serviec="https://google.com",
        contact=openapi.Contact(email="thuytt7@vng.com.vn"),
        license=openapi.License(name = "EP License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('epns/', schema_view.with_ui('swagger', cache_timeout=0), name='epns'),
    path('slack', SlackView.as_view(), name='slack'),
    path('outlook', OutlookView.as_view(), name='outlook'),
    path('teams', TeamsView.as_view(), name='teams'),
    path('telegram', TelegramView.as_view(), name='telegram')
]
