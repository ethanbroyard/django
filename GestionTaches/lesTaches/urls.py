

from django.urls import path
from django.contrib import admin
from . import views

app_name="lesTaches"
urlpatterns = [
    
    path("home", views.home, name="home"),
    path("home/<name>", views.home, name="name"),
    path("taches/", views.task_listing,name="listing"),
    path("taches/details/<tache_id>", views.details,name="details"),
    # path("taches/ajout", views.ajout,name="ajout"),
    path('taches/create/', views.TaskCreate.as_view(), name='task-create'),
    path('taches/<int:pk>/update/', views.TaskUpdate.as_view(), name='task-update'),
    path('taches/<int:pk>/delete/', views.TaskDelete.as_view(), name='task-delete'),
    path("admin/", admin.site.urls),
]