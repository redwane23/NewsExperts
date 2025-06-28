from .base import *

from pathlib import Path


SECRET_KEY='django-insecure-a74oz2lxi&zzy$eme!z+wzuh)3g4ylmvd#t8@1$*z_o^pqu=&v'
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}