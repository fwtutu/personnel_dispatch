# 在 temp_worker/urls.py
from django.urls import path
from . import views
from .views import edit_profile_view
from schedule_system.views import ScheduleCreateView


urlpatterns = [
    path('', views.temp_worker_home, name='temp_worker_home'),
    path('profile/<int:user_id>/', views.personnel_profile, name='profile'),
    path('profile/<int:user_id>/edit/', views.edit_profile_view, name='edit_profile'),
    path('schedule/create_schedule/', ScheduleCreateView.as_view(), name='create_schedule'),  # 對應 app2 的第二個視圖

]
