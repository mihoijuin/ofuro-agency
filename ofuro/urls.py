from django.contrib.auth.views import login, logout
from django.urls import path

from . import views
from .crypturl import AESCipher

app_name = 'ofuro'
key = 'poriporiporiofuroporipori'
aes = AESCipher(key)

# 結局うけつけるのはpathで指定した内容なので複合化意味なくね？ってなった
urlpatterns = [
    path('', views.top, name='top'),
    # path('result', views.result, name='result'),
    # ! BOT使わなくなったので下記はコメントアウト
    # path('', login, {'template_name': 'top.html', }, name='top'),
    # めんどいのでログアウト後の画面はトップにしちゃった
    # ログアウトしたらアラートで「ログアウトしました」って出たら理想
    # path('logout', logout, {'template_name': 'top.html', }, name='top'),
    # path('ordered', views.ordered, name='ordered'),    # Twitter認証後リダイレクト
    path('LofG1lC3uIf7XnD6awGDw==', views.result_monkey, name='result_monkey'),
    path(aes.encrypt(aes.key,'result-dog'), views.result_dog, name='result_dog'),
    path(aes.encrypt(aes.key,'result-duck'), views.result_duck, name='result_duck'),
    path(aes.encrypt(aes.key,'result-nananana'), views.result_nananana, name='result_nananana'),
    path(aes.encrypt(aes.key,'result-money'), views.result_money, name='result_money'),
    path(aes.encrypt(aes.key,'result-oyaji'), views.result_oyaji, name='result_oyaji'),
    path(aes.encrypt(aes.key,'result-momu'), views.result_momu, name='result_momu'),
    path(aes.encrypt(aes.key,'result-sana'), views.result_sana, name='result_sana'),
    path('gunY0ZDCpndh1PkTaRRNw==', views.result_mam, name='result_mam'),
    path('mmDtzcWuWnC0pYkMBEugKgR5rXLRQRKv02WLfTIvzM=', views.result_seabiscuit, name='result_seabiscuit'),
    path('wait', views.wait, name='wait'),    # 例外発生時にリダイレクト
]
