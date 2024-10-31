from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm


def home(request):
    return render(request, 'personnel_management/home.html')

    
# def update_employee(request, employee_id):
#     employee = get_object_or_404(Employee, id=employee_id)

#         if request.method == 'POST':
#             form = EmployeeForm(request.POST, instance=employee)
#             if form.is_valid():
#                 form.save()
#                 return redirect('employee_list')  # 更新成功後重定向到首頁
#         else:
#         form = EmployeeForm(instance=employee)

#     return render(request, 'personnel_management/update_employee.html', {'form': form, 'employee': employee})


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