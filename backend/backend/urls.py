from django.contrib import admin
from django.urls import path, re_path

from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    re_path(r'^api/pets/$', views.pet_list),
    re_path(r'^api/pets/([0-9])$', views.pets_detail)
]
