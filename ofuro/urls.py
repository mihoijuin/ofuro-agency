from django.urls import path
from django.contrib.auth.views import login
from . import views

app_name = 'ofuro'

urlpatterns = [
    path('', login, {'template_name': 'ofuro/top.html', }, name='top'),
    path('orderd', views.orderd, name='orderd'),    # Twitter認証後リダイレクト
    path('result', views.result, name='result'),
    path('wait', views.wait, name='wait'),    # 例外発生時にリダイレクト
]
