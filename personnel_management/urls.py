from django.urls import path
from .views import home, update_employee ,employee_list,ScheduleListView,ScheduleDeleteView,ScheduleListData, match_appointment
from . import views



urlpatterns = [
    path('', home, name='home'),
    path('update_employee/<int:employee_id>/', update_employee, name='update_employee'),  # 更新員工資料
    path('employees/', employee_list, name='employee_list'),  # 員工列表視圖
    path('schedule/', ScheduleListView.as_view(), name='schedule_list'),
    path('schedule/delete/<int:pk>/', ScheduleDeleteView.as_view(), name='schedule_delete'),  # 刪除URL
    path('api/ScheduleListData/',views.ScheduleListData, name='ScheduleListData'),
    path("customers/", views.customer_list, name="customer_list"),
    path('customers/<int:customer_id>/appointments/', views.customer_appointments, name='customer_appointments'),
    path("match_appointment/<int:appointment_id>/", views.match_appointment, name="match_appointment")
    
]
