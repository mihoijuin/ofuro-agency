from django.contrib.auth.views import login, logout
from django.urls import path

from . import views

app_name = 'ofuro'

urlpatterns = [
    path('', login, {'template_name': 'top.html', }, name='top'),
    # めんどいのでログアウト後の画面はトップにしちゃった
    # ログアウトしたらアラートで「ログアウトしました」って出たら理想
    path('logout', logout, {'template_name': 'top.html', }, name='top'),
    path('ordered', views.ordered, name='ordered'),    # Twitter認証後リダイレクト
    path('result-monkey', views.result_monkey, name='result_monkey'),
    path('result-dog', views.result_dog, name='result_dog'),
    path('result-duck', views.result_duck, name='result_duck'),
    path('result-nananana', views.result_nananana, name='result_nananana'),
    path('result-money', views.result_money, name='result_money'),
    path('result-oyaji', views.result_oyaji, name='result_oyaji'),
    path('wait', views.wait, name='wait'),    # 例外発生時にリダイレクト
]
