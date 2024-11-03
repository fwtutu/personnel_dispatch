from django.urls import path
from .views import ScheduleCreateView,UserScheduleListView

urlpatterns = [
    path('schedule/create_schedule/', ScheduleCreateView.as_view(), name='create_schedule'),
    # path('schedule/', ScheduleListView.as_view(), name='list_schedule'),  # 排班列表頁
    path('schedule/user_schedule_list/', UserScheduleListView.as_view(), name='user_schedule_list'),  # 個人排班列表
]
