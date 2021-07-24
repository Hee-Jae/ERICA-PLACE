from django.urls import path
from . import views

urlpatterns = [

    path('<int:room_id>', views.reservation, name = "rsv"),
    path('form/<int:room_id>', views.form, name = "form"),
    path('create', views.create, name = "create"),
]

