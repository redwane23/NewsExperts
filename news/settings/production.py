from pathlib import Path
import os


SECRET_KEY='django-insecure-a74oz2lxi&zzy$eme!z+wzuh)3g4ylmvd#t8@1$*z_o^pqu=&v'
DEBUG = False

ALLOWED_HOSTS = ["newsexperts.onrender.com"]

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'True') == 'False'
import dj_database_url

