"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("common/", include("common.urls")),
    path("accounts/", include("accounts.urls")),
    path("dist_app/", include("dist_app.urls")),
    path("recommend_app/", include("recommend_app.urls")),
    path("schedule_app/", include("schedule_app.urls")),
    path("home_app/",include("home_app.urls"))


    # path('dist_app/', include('dist_app.urls')),
    # path('home/', include('home_app.urls')),
    # path('mypage/', include('mypage.urls')),
    # path('recommend_app/', include('recommend_app.urls')),
    # path('schdule_app/', include('schdule_app.urls'))
]
