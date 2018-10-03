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
    path('result-monkey', views.result-monkey, name='result-monkey'),
    path('result-dog', views.result-dog, name='result-dog'),
    path('result-duck', views.result-duck, name='result-duck'),
    path('result-nananana', views.result-nananana, name='result-nananana'),
    path('result-money', views.result-money, name='result-money'),
    path('result-oyaji', views.result-oyaji, name='result-oyaji'),
    path('wait', views.wait, name='wait'),    # 例外発生時にリダイレクト
]
