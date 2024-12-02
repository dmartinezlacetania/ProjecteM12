from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    path('exercise/list', views.exercise_list, name='exercise_list'),
    path('exercise/create', views.exercise_create, name='exercise_create'),
    path('exercise/edit/<int:exercise_id>', views.exercise_edit, name='exercise_edit'),
    path('routine/list', views.routine_list, name='routine_list'),
    path('routine/create', views.routine_create, name='routine_create'),
    # path('routine/edit/<int:routine_id>', views.routine_edit, name='routine_edit'),
    # path('routine/delete/<int:routine_id>', views.routine_delete, name='routine_delete'),
]