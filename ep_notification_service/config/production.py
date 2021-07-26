import os

import dj_database_url

from .common import Common


class Production(Common):
    INSTALLED_APPS = Common.INSTALLED_APPS
    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
    # Site
    # https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ["*"]

    POSTGRES_DB = os.getenv('POSTGRES_DB')
    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST')
    DATABASE_URL = f'postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}'
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=int(os.getenv('POSTGRES_CONN_MAX_AGE', 600))
        )
    }

    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://redis:6379/1",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        }
    }

    CELERY_BROKER_URL = 'amqp://rabbitmq:5672'
