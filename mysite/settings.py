import os
from socket import gethostname

import django_heroku
import dj_database_url

# HOSTNAME
HOSTNAME = gethostname()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# シークレットキー読み込み＠開発環境
if 'local' in HOSTNAME:
    import local_settings
    SECRET_KEY = local_settings.SECRET_KEY
else:
    SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',    # Heroku
    'django.contrib.staticfiles',
    'ofuro',    # app
    'social_django',    # Twitter認証用
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',   # heroku
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Twitter認証用
                'social_django.context_processors.backends',
                # Twitter認証用
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Heroku
# Change 'default' database configuration with $DATABASE_URL.
DATABASES['default'].update(dj_database_url.config(conn_max_age=500, ssl_require=True))

# Heroku
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# heroku
STATIC_ROOT = os.path.join(BASE_DIR, 'ofuro/staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'ofuro/static'),
)

# Heroku
# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Twitter認証用
AUTHENTICATION_BACKENDS = [
    'social_core.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
]


if 'local' in HOSTNAME:
    import local_settings
    # Twitter認証用キー
    SOCIAL_AUTH_TWITTER_KEY = local_settings.SOCIAL_AUTH_TWITTER_KEY   # Consumer Key
    SOCIAL_AUTH_TWITTER_SECRET = local_settings.SOCIAL_AUTH_TWITTER_SECRET  # Consumer Secret
    SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/ordered'    # リダイレクトURL
    # BOT用キー
    CK = local_settings.CK
    CS = local_settings.CS
    AT = local_settings.AT
    ATS = local_settings.ATS
else:
    # Twitter認証キー
    SOCIAL_AUTH_TWITTER_KEY = os.environ['SOCIAL_AUTH_TWITTER_KEY']
    SOCIAL_AUTH_TWITTER_SECRET = os.environ['SOCIAL_AUTH_TWITTER_SECRET']
    SOCIAL_AUTH_LOGIN_REDIRECT_URL = os.environ['SOCIAL_AUTH_LOGIN_REDIRECT_URL']
    # BOT用のキー
    CK = os.environ['CK']
    CS = os.environ['CS']
    AT = os.environ['AT']
    ATS = os.environ['ATS']



# Heroku
DEBUG = False

try:
    from .local_settings import *
except ImportError:
    pass


django_heroku.settings(locals())
