from django.urls import path
from .views import ScheduleCreateView

urlpatterns = [
    path('schedule/create_schedule/', ScheduleCreateView.as_view(), name='create_schedule'),
    # path('schedule/', ScheduleListView.as_view(), name='list_schedule'),  # 排班列表頁

]
