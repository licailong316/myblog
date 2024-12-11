from .base import *  # NOQA

DEBUG = False

ALLOWED_HOSTS = ["licailong.cn", "www.licailong.cn", "127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'HOST': '127.0.0.1',
        'USER': 'licailong',
        'PASSWORD': '316licailongLCL@',
        'PORT': 3306,
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}
