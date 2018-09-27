import os

from dj_static import Cling
from django.core.wsgi import get_wsgi_application

# TODO Djangoかwhitenoiseのバージョンの問題でインポートエラー発生するので後で調べて書き直す


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = Cling(get_wsgi_application())


