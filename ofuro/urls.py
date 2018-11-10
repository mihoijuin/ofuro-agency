from django.contrib.auth.views import login, logout
from django.urls import path

from . import views
from .crypturl import AESCipher

app_name = 'ofuro'
aes = AESCipher()

# 結局うけつけるのはpathで指定した内容なので複合化意味なくね？ってなった
urlpatterns = [
    path('', views.top, name='top'),
    path('wait', views.wait, name='wait'),    # 例外発生時にリダイレクト
    path('page-transition', views.page_transition, name='page_transition'),
    path('results/<str:pk>', views.result_detail, name='result_detail'),
    path('{}'.format(aes.encrypt('ain')), views.result_detail),
]
