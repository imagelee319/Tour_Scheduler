from django.urls import path
from . import views

app_name = 'mypage_app'

urlpatterns = [
    path("index/",views.index, name = "index"),
    path("update/", views.UPDATEView, name = "update"),
    

    
]