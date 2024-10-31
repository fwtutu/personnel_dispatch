# 在 temp_worker/urls.py
from django.urls import path
from . import views
from .views import edit_profile_view

urlpatterns = [
    path('', views.home, name='temp_worker_home'),
    path('profile/<int:user_id>/', views.personnel_profile, name='profile'),
    path('profile/<int:user_id>/edit/', views.edit_profile_view, name='edit_profile'),

]
