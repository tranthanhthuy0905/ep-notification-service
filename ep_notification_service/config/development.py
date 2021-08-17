import os

import dj_database_url

from .common import Common


class Development(Common):
    INSTALLED_APPS = Common.INSTALLED_APPS
