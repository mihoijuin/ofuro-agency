from django.contrib.auth.views import login, logout
from django.urls import path, re_path

from . import views
from .crypturl import AESCipher

app_name = 'ofuro'
aes = AESCipher()

# 結局うけつけるのはpathで指定した内容なので複合化意味なくね？ってなった
urlpatterns = [
    path('', views.top, name='top'),
    path('page-transition', views.page_transition, name='page_transition'),
    # re_path(r'^results/(?P<enc_pk>[_!(%=0-9a-zA-Z])/$', views.page_transition, name='page_transition'),
    path('results/<str:enc>', views.result_detail, name='result_detail'),
    path('{}'.format(aes.encrypt('dog')), views.result_detail),
]
