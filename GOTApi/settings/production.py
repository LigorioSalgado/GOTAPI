from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'got_db',
        'USER': 'got_admin',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
STATIC_URL = '/static/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

