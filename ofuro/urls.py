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
    path('result1', views.result1, name='result1'),
    path('result2', views.result2, name='result2'),
    path('result3', views.result3, name='result3'),
    path('wait', views.wait, name='wait'),    # 例外発生時にリダイレクト
]
