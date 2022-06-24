from django.urls import path
from . import views
from .views import finallist

app_name = 'schedule_app'

urlpatterns = [
    path("index/", views.index, name='index'),
    path("list/", views.schedulelist, name='list'),
    path("create/", views.create, name='create'),
    path("day/", views.day, name='day'),
    path("finallist/", views.finallist, name='finallist'),
    path('delete/<int:place_author_ad>', views.delete, name='delete')
]