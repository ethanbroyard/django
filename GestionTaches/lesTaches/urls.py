

from django.urls import path
from django.contrib import admin
from . import views

app_name="lesTaches"
urlpatterns = [
    
    path("home", views.home, name="home"),
    path("home/<name>", views.home, name="name"),
    path("taches/", views.task_listing,name="listing"),
    path("taches/details/<tache_id>", views.details,name="details"),
    path("taches/ajout", views.ajout,name="ajouts"),
    path("admin/", admin.site.urls),
]