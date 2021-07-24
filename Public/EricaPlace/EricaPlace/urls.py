"""EricaPlace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import main.views
import faq.views
import rsv.views
import status.views
import director.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.main, name="main"),
    path('useGuide/', main.views.useGuide, name="useGuide"),
    path('mainplace/', main.views.mainplace, name="mainplace"),
    path('building/', main.views.building, name="building"),
    path('faq', faq.views.faq, name="faq"),
    path('roomlist/<int:building_id>',main.views.roomlist, name = "roomlist"),
    path('recommend/<int:purpose_id>',main.views.recommend, name = "recommend"),
    path('headcount/<int:count>', main.views.headcount, name="headcount"),

    path('status/', include('status.urls')),
    path('reservation/', include('rsv.urls')),
    path('login/', director.views.login, name="director_login"),
    path('logout/', director.views.logout, name="director_logout"),
    path('director/', include('director.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
