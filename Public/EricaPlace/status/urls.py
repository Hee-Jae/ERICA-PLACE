from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.status, name="status"),
    path('list/', views.status_list, name = "status_list"),
    path('remove/<int:rsv_id>', views.remove, name = "remove"),
]

