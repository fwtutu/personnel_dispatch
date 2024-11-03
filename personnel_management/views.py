from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from schedule_system.models import Schedule # 引入 Employee 模型
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.http import JsonResponse


def home(request):
    return render(request, 'personnel_management/home.html')


def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)  # 使用 POST 數據和當前員工實例來創建表單
        if form.is_valid():
            form.save()  # 保存更新
            return redirect('employee_list')  # 重定向到員工列表
    else:
        form = EmployeeForm(instance=employee)  # 獲取當前員工實例的表單以便顯示現有數據

    return render(request, 'personnel_management/update_employee.html', {'form': form})


def employee_list(request):
    employees = Employee.objects.all()  # 獲取所有員工資料
    return render(request, 'personnel_management/employee_list.html', {'employees': employees})


class ScheduleListView(ListView):
    model = Schedule
    template_name = 'personnel_management/schedule_list.html'  # 模板路徑
    context_object_name = 'schedules'
    ordering = ['start_datetime']  # 依據開始時間排序
    paginate_by = 10  # 每頁顯示 10 條記錄

    
class ScheduleDeleteView(DeleteView):
    model = Schedule
    template_name = 'personnel_management/schedule_confirm_delete.html'
    success_url = reverse_lazy('schedule_list')  # 刪除成功後重導向的URL


def ScheduleListData(request):
    schedules = Schedule.objects.all()  # 獲取所有排班資料
    events = []
    for schedule in schedules:
        events.append({
            "title": schedule.calendar_title if schedule.calendar_title else schedule.employee.name,  # 使用日曆標題或員工名稱
            "start": schedule.start_datetime.isoformat(),
            "end": schedule.end_datetime.isoformat(),
            "extendedProps": {
                "hoursWorked": schedule.hours_worked  # 工時
            }
        })
    return JsonResponse(events, safe=False)