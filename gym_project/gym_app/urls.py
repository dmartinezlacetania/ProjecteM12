from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register , name='register'),
    path('login/', views.user_login, name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('admin/', admin.site.urls),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]