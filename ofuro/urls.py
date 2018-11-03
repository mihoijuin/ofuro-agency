from django.contrib.auth.views import login, logout
from django.urls import path

from . import views
from .crypturl import AESCipher

app_name = 'ofuro'
aes = AESCipher()

# 結局うけつけるのはpathで指定した内容なので複合化意味なくね？ってなった
urlpatterns = [
    path('', views.top, name='top'),
    path('page-transition', views.page_transition, name='page_transition'),
    path(aes.encrypt('result-monkey'), views.result_monkey, name='result_monkey'),
    path(aes.encrypt('result-dog'), views.result_dog, name='result_dog'),
    path(aes.encrypt('result-duck'), views.result_duck, name='result_duck'),
    path(aes.encrypt('result-nananana'), views.result_nananana, name='result_nananana'),
    path(aes.encrypt('result-muscle_nananana'), views.result_muscle_nananana, name='result_muscle_nananana'),
    path(aes.encrypt('result-money'), views.result_money, name='result_money'),
    path(aes.encrypt('result-oyaji'), views.result_oyaji, name='result_oyaji'),
    path(aes.encrypt('result-momu'), views.result_momu, name='result_momu'),
    path(aes.encrypt('result-sana'), views.result_sana, name='result_sana'),
    path(aes.encrypt('result-chihiro'), views.result_chihiro, name='result_chihiro'),
    path(aes.encrypt('result-higuma'), views.result_higuma, name='result_higuma'),
    path(aes.encrypt('result-yukariko'), views.result_yukariko, name='result_yukariko'),
    path(aes.encrypt('result-sorami'), views.result_sorami, name='result_sorami'),
    path(aes.encrypt('result-mokyu'), views.result_mokyu, name='result_mokyu'),
    path(aes.encrypt('result-imari'), views.result_imari, name='result_imari'),
    path(aes.encrypt('result-momiji'), views.result_momiji, name='result_momiji'),
    path(aes.encrypt('result-ain'), views.result_ain, name='result_ain'),
    path(aes.encrypt('result-mareru'), views.result_mareru, name='result_mareru'),
    path(aes.encrypt('result-haijoi'), views.result_haijoi, name='result_haijoi'),
    path(aes.encrypt('result-beryl'), views.result_beryl, name='result_beryl'),
    path(aes.encrypt('result-amanatu'), views.result_amanatu, name='result_amanatu'),
    path(aes.encrypt('result-mam'), views.result_mam, name='result_mam'),
    path(aes.encrypt('result-seabiscuit'), views.result_seabiscuit, name='result_seabiscuit'),
    path('wait', views.wait, name='wait'),    # 例外発生時にリダイレクト
]
