from django.urls import path
from django.contrib.auth.views import login
from . import views

app_name = 'ofuro'

urlpatterns = [
    path('', login, {'template_name': 'top.html', }, name='top'),
    path('ordered', views.ordered, name='ordered'),    # Twitter認証後リダイレクト
 #   path('result1', views.result1, name='result1'),
 #   path('result2', views.result2, name='result2'),
 #   path('result3', views.result1, name='result3'),
    path('wait', views.wait, name='wait'),    # 例外発生時にリダイレクト
]
