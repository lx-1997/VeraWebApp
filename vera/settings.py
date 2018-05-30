"""
Django settings for vera project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'btcha4=9_!7*hhjka8b^m2cjih06y0amiin-ftcaweq$myl(g8_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jobboard',
    'candidateprofile',
    'vacancy',
    'quiz',
    'interview',
    'account',
    'statistic',
    'material',
    'material.frontend',
    'django_filters',
    'pipeline',
    'company',
    'google_address',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'jobboard.v_middleware.NodeMiddleware',
    'jobboard.v_middleware.RoleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'account.middleware.LocaleMiddleware',
    # 'account.middleware.TimezoneMiddleware',
]

ROOT_URLCONF = 'vera.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'account.context_processors.account',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'jobboard.context_processors.roles',
                'jobboard.context_processors.hints',
            ],
        },
    },
]

WSGI_APPLICATION = 'vera.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'statistic': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'statistic.sqlite3'),
    }
}

DATABASE_ROUTERS = ['jobboard.database_router.DBRouter', 'jobboard.database_router.PrimaryRouter']

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_FROM_EMAIL = 'you@domain.com'

THEME_CONTACT_EMAIL = 'VeraOracle@email.com'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

VERA_COIN_CONTRACT_ADDRESS = '0xD1d0cb0eC75F005B54984B94bA7EC45857Df81Ea'  # Rinkeby

VERA_COIN_PRESALE_CONTRACT_ADDRESS = '0x11535d665C841b9A067EDbBBDEcD81E091f442f2'  # Rinkeby

VERA_ORACLE_CONTRACT_ADDRESS = '0x43e51d724827b0cd06f294c2dbe038a955ab6223'  # Rinkeby

WEB_ETH_COINBASE = '0x8dC270b448958fEd366E0eDfb28B335Bf84fCA91'  # Rinkeby

NODE_URL = 'http://localhost:8545'

NET_URL = 'https://rinkeby.etherscan.io/'

LOGIN_URL = '/account/login'

W2V_API_URL = 'http://52.166.10.44:3000/getvecw2v'

SESSION_SAVE_EVERY_REQUEST = True

CHAT_WS_SERVER_HOST = '192.168.254.240'

CHAT_WS_SERVER_PORT = 5002

CHAT_WS_SERVER_PROTOCOL = 'ws'

ACCOUNT_OPEN_SIGNUP = True

# Hints settings
HINTS_ENABLED = True

# Google address settings
GOOGLE_ADDRESS = {
    'API_KEY': '',
    'API_LANGUAGE': 'en_US'
}

GOOGLE_JS_MAP_KEY = ''

# Social icons
# icon name on fontawesome, exm: 'www.<ok>.ru' -> <i class="fa fa-<odnoklassniki>"></i>
SOCIAL_ICONS = {
    'ok': 'odnoklassniki-square',
    'facebook': 'facebook-official',
    't': 'telegram',
    'steamcommunity': 'steam-square',
}

if DEBUG:
    try:
        from vera.local_settings import *
    except Exception:
        pass
