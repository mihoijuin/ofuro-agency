from django.contrib.auth.views import login, logout
from django.urls import path

from . import views
from .crypturl import AESCipher

app_name = 'ofuro'
key = 'poriporiporiofuroporipori'
aes = AESCipher(key)

urlpatterns = [
    path('', login, {'template_name': 'top.html', }, name='top'),
    # めんどいのでログアウト後の画面はトップにしちゃった
    # ログアウトしたらアラートで「ログアウトしました」って出たら理想
    path('logout', logout, {'template_name': 'top.html', }, name='top'),
    path('ordered', views.ordered, name='ordered'),    # Twitter認証後リダイレクト
    path(aes.encrypt(aes.key,'result-monkey'), views.result_monkey, name='result_monkey'),
    path(aes.encrypt(aes.key,'result-dog'), views.result_dog, name='result_dog'),
    path(aes.encrypt(aes.key,'result-duck'), views.result_duck, name='result_duck'),
    path(aes.encrypt(aes.key,'result-nananana'), views.result_nananana, name='result_nananana'),
    path(aes.encrypt(aes.key,'result-money'), views.result_money, name='result_money'),
    path(aes.encrypt(aes.key,'result-oyaji'), views.result_oyaji, name='result_oyaji'),
    path('wait', views.wait, name='wait'),    # 例外発生時にリダイレクト
]
