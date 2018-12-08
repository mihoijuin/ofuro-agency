from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'ofuro'

# 結局うけつけるのはpathで指定した内容なので複合化意味なくね？ってなった
urlpatterns = [
    path('', views.top, name='top'),
    path('page-transition', views.page_transition, name='page_transition'),
    path('results/<str:enc>', views.result_detail, name='result_detail'),
    path('staffs', views.staffs, name='staffs'),
    path('wait', views.wait, name='wait'),
]

# メディアファイル公開用のURL
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
