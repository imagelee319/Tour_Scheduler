
from django.urls import path
from . import views

app_name = 'dist_app'

urlpatterns = [
    path("index/",views.index, name = "index"),
    path("index2/",views.index_2, name = "index2"),
    path("index3/",views.index_3, name = "index3"),
    path("marker/",views.marker, name = "marker"),
    path('jeju/', views.jeju, name='jeju'),
    path('aewol/', views.aewol, name='aewol'),
    path('hanlim/', views.hanlim, name='hanlim'),
    path('hankyung/', views.hankyung, name='hankyung'),
    path('daejung/', views.daejung, name='daejung'),
    path('andeok/', views.andeok, name='andeok'),
    path('jungmun/', views.jungmun, name='jungmun'),
    path('seogwipo/', views.seogwipo, name='seogwipo'),
    path('namwon/', views.namwon, name='namwon'),
    path('pyosun/', views.pyosun, name='pyosun'),
    path('seongsan/', views.seongsan, name='seongsan'),
    path('gujwa/', views.gujwa, name='gujwa'),
    path('jocheon/', views.jocheon, name='jocheon'),
]