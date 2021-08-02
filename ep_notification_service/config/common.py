
import os
from dotenv import load_dotenv
load_dotenv()
from os.path import join
import dj_database_url
from datetime import timedelta
from configurations import Configuration
from distutils.util import strtobool

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Common(Configuration):
    # SECURITY WARNING: keep the secret key used in production secret!
    # SECRET_KEY = 'django-insecure-l)ec!&tdj97d97m4a09vf-cuf=lc!9e@%nje7h)g!1oe!#rvf7'
    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
    WSGI_APPLICATION = 'ep_notification_service.wsgi.application'
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = strtobool(os.getenv('DJANGO_DEBUG', 'no'))

    ALLOWED_HOSTS = ['*']


    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # thirst-party application
        'rest_framework',
        'drf_yasg',

        # own application
        'notification',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'ep_notification_service.urls'

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/

    STATIC_ROOT = os.path.normpath(join(os.path.dirname(BASE_DIR), 'static'))
    STATICFILES_DIRS = []
    STATIC_URL = '/static/'
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    TEMPLATE_PATH = os.path.normpath(join(os.path.dirname(BASE_DIR), 'templates'))

    # Media files
    MEDIA_ROOT = join(os.path.dirname(BASE_DIR), 'templates')
    MEDIA_URL = '/templates/'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': STATICFILES_DIRS,
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    # Email
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    ADMINS = (
        ('Author', 'thuytt7@vng.com.vn'),
    )

    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

    DATABASES = {
            'default': dj_database_url.config(
                default='postgres://postgres:postgres@localhost:5432/epns',
                conn_max_age=int(os.getenv('POSTGRES_CONN_MAX_AGE', 600))
            )
        }

    REST_FRAMEWORK = {
        'TEST_REQUEST_DEFAULT_FORMAT': 'json',
        'TEST_REQUEST_RENDERER_CLASSES': [
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.TemplateHTMLRenderer'
        ]
    }

    # Password validation
    # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    SWAGGER_SETTINGS = {
            'SECURITY_DEFINITIONS': {
                'api_key': {
                    'type': 'apiKey',
                    'in': 'header',
                    'name': 'Authorization'
                }
            },
        }

    LOG_DIR = os.path.join(BASE_DIR, '..', 'logs')
    # Logging
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'django.server': {
                '()': 'django.utils.log.ServerFormatter',
                'format': '[%(server_time)s] %(message)s',
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
            "standard": {
                "format": "%(asctime)s %(name)s %(levelname)s %(message)s",
                "datefmt": "%Y-%m-%dT%H:%M:%S%z",
            },
            "json": {
                "format": "%(asctime)s %(name)s %(levelname)s %(message)s",
                "datefmt": "%Y-%m-%dT%H:%M:%S%z",
                "class": "pythonjsonlogger.jsonlogger.JsonFormatter"
            }
        },
        'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'handlers': {
            'django.server': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'django.server',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'json'
            },
            'access': {
                'level': 'INFO',
                'filename': os.path.join(LOG_DIR, 'access.log'),
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'when': 'midnight',  # 1024 * 1024 * 15B = 15MB
                'backupCount': 10,
                'formatter': 'standard',
            },
            'error': {
                'level': 'ERROR',
                'filename': os.path.join(LOG_DIR, 'error.log'),
                'class': 'logging.handlers.TimedRotatingFileHandler',
                # 'maxBytes': 15728640,  # 1024 * 1024 * 15B = 15MB
                'when': 'midnight',
                'backupCount': 10,
                'formatter': 'standard',
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'propagate': False,
            },
            'django.server': {
                'handlers': ['console', 'access'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'django.request': {
                'handlers': ['console', 'error'],
                'level': 'ERROR',
                'propagate': False,
            },
            'django.db.backends': {
                'handlers': ['console', 'access'],
                'level': 'INFO'
            },
            'ep_notification_service': {
                'handlers': ['console', 'access', 'error'],
                'level': 'DEBUG',
                'propagate': False,
            }
        }
    }
    # Internationalization
    # https://docs.djangoproject.com/en/3.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Default primary key field type
    # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    # SLACK CONFIGURATION
    #SLACK_URL_WEBHOOK = os.getenv('SLACK_URL_WEBHOOK')

    # MICROSOFT TEAMS CONFIGURATION
    #TEAMS_URL_WEBHOOK = os.getenv('TEAMS_URL_WEBHOOK')

    # OUTLOOK CONFIGURATION
    # Add Protocol which encrypts and delivers mail securely
    EMAIL_USE_TLS = True
    # Replace the email of the server used here
    EMAIL_HOST = os.getenv('EMAIL_HOST')
    EMAIL_PORT = os.getenv('EMAIL_PORT')
    # The sender's email address
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

    SERVER_EMAIL = EMAIL_HOST_USER

    # TELEGRAM CONFIGURATION
    # TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    # TELEGRAM_CHATID = os.getenv('TELEGRAM_CHATID')
