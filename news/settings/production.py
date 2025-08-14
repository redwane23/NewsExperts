from .base import *
from pathlib import Path
import os


DEBUG = False

ALLOWED_HOSTS = ["newsexperts.onrender.com"]
DEBUG ='False'
import dj_database_url

DATABASES = {
      'default': dj_database_url.config(
          default='postgresql://redwane:mKcDplSkHavcUqV4eTxDNQfTelEl6i6H@dpg-d166cojuibrs73bd0130-a/newsexperts',
          conn_max_age=600
      )
}
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "default",
    }
}