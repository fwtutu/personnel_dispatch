# 在 temp_worker/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import EmployeeProfile
from personnel_management.forms import EmployeeForm
from users.models import User
from .models import Employee
from django.shortcuts import render, get_object_or_404
from django.urls import reverse



@login_required
def home(request):
    user = request.user  # 取得目前登入的使用者
    context = {
        'username': user.username,
        'user_id': user.id,
        # 可以加入更多和使用者相關的資訊
    }
    return render(request, 'temp_worker/home.html', context)

# 待確認修改
@login_required
def personnel_profile(request, user_id):
    user = request.user 
    # 確保僅允許當前登入的使用者訪問其自己的資料
    if user.id != user_id:
        return redirect('temp_worker_home')
    # 嘗試取得對應的 Employee 對象    
    try:
        employee = Employee.objects.get(user_id=user_id)  # user id 獲取 Employee 
        form = EmployeeForm(instance=employee)  # 已有資料時顯示該資料
    except Employee.DoesNotExist:
        # 尚未創建 Employee，顯示空表單
        form = EmployeeForm()
            
# 將 form 和 employee 傳遞給模板，讓模板可以根據有無資料進行顯示
    return render(request, 'temp_worker/profile.html', {'form': form, 'employee': employee if 'employee' in locals() else None})

def edit_profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    employee, created = Employee.objects.get_or_create(user=user)  # 確保獲取或創建一個Employee對象

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('profile', user_id=user.id)
    else:
        form = EmployeeForm(instance=employee)
    
    return render(request, 'temp_worker/edit_profile.html', {'form': form})

