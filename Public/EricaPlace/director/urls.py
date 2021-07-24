from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
  path('status/', views.status, name="director_status"),
  path('create_room/<int:building_id>', views.create_room, name="create_room"),
  path('update_room/<int:room_id>', views.update_room, name="update_room"),
  path('create_building/', views.create_building, name="create_building"),
  path('update_building/<int:building_id>', views.update_building, name="update_building"),
  path('create_question/', views.create_question, name="create_question"),
  path('update_question/<int:faq_id>', views.update_question, name="update_question"),
  path('rsv_admit/<int:rsv_id><int:type>', views.rsv_admit, name="rsv_admit"),
  path('modify/', views.modify, name = "modify"),
  path('modify_building/', views.modify_building, name="modify_building"),
  path('modify_faq/', views.modify_faq, name="modify_faq"),
  path('delete_faq/<int:faq_id>', views.delete_faq, name="delete_faq"),
  path('delete_building/<int:building_id>', views.delete_building, name= "delete_building"),
  path('delete_room/<int:room_id>', views.delete_room, name= "delete_room"),
  path('building_list/', views.building_list, name = "building_list"),
  path('modify_room/<int:building_id>', views.modify_room, name = "modify_room"),
]