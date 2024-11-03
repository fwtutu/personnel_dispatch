from django.urls import path
from .views import home, update_employee ,employee_list,ScheduleListView,ScheduleDeleteView,ScheduleListData
from . import views



urlpatterns = [
    path('', home, name='home'),
    path('update_employee/<int:employee_id>/', update_employee, name='update_employee'),  # 更新員工資料
    path('employees/', employee_list, name='employee_list'),  # 員工列表視圖
    path('schedule/', ScheduleListView.as_view(), name='schedule_list'),
    path('schedule/delete/<int:pk>/', ScheduleDeleteView.as_view(), name='schedule_delete'),  # 刪除URL
    path('api/ScheduleListData/',views.ScheduleListData, name='ScheduleListData'),

]
