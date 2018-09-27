import os

from django.core.wsgi import get_wsgi_application

# TODO Djangoかwhitenoiseのバージョンの問題でインポートエラー発生するので後で調べて書き直す
from whitenoise.django import DjangoWhiteNoise    # Herokuデプロイ用

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()

application = DjangoWhiteNoise(application)   # Herokuデプロイ用
