from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponseForbidden
from functools import wraps
from .models import Rank
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from personnel_management.models import Employee


# 首頁
def users_home(request):
    return render(request, "home.html")

# 註冊功能
def register(request):
    user = request.user
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():  # 驗證表單
            user = form.save()  # 創建用戶
            print(f"Created user: {user.username}, user_id: {user.id}")  
            Rank.objects.get_or_create(user=user)  # 檢查用戶是否已經有 Rank  如果不存在則創建 創建 Rank，並默認角色為管理員
            # login(request, user)  # 登入用戶
            # messages.success(request, "註冊成功！您已成功登入。")  # 註冊成功訊息
            # 創建相應的 Employee 記錄
            Employee.objects.create(
                name='',  # 可以根據需求設置為空
                age=None,  # 設為 None 或其他空值
                contact_number='',
                address='',
                user_id=user.id  # 將 user_id 連接到 Employee
            )

            return redirect("users_home")  # 成功後重定向到首頁
        else:
            messages.error(request, "註冊失敗，請檢查您的資料。")  # 註冊失敗訊息    
    else:
        form = RegisterForm()  # 初始化空表單
        
    return render(request, "register.html", {"form": form})


# 登錄功能
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.success(request, "登入成功！")  # 登入成功訊息
                return redirect("login_success")  # 登入成功跳轉登入成功頁面
            else:
                messages.error(request, "登入失敗，請檢查您的使用者名稱和密碼。")  # 登入失敗訊息
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

# 登錄成功頁面

@login_required 
def login_success(request):
    return render(request, "login_success.html")

from django.contrib.auth import logout

def logout_view(request):
    logout(request)  # 退出登入
    return redirect("home")  # 登出後跳轉首頁


# 用戶角色判定
def role_required(*allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                rank = Rank.objects.get(user=request.user)
                if rank.role in allowed_roles:
                    return view_func(request, *args, **kwargs)
            return HttpResponseForbidden()  # 403 Forbidden
        return _wrapped_view
    return decorator


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
@role_required('admin')
def manage_roles(request):
    users = User.objects.all()  # 獲取所有用戶
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        new_role = request.POST.get("role")
        user = User.objects.get(id=user_id)
        rank = Rank.objects.get(user=user)
        rank.role = new_role  # 更新角色
        rank.save()
        return redirect("manage_roles")  # 重新加載角色管理頁面
        # 確保 Rank 存在
    try:
        rank = Rank.objects.get(user=user)
        rank.role = new_role  # 更新角色
        rank.save()
        
    except Rank.DoesNotExist:
        # 如果 Rank 不存在，則可選擇記錄日誌或返回錯誤消息
        print(f"Rank for user {user.username} does not exist.")
        return redirect("manage_roles")  # 重定向以避免頁面崩潰

    return render(request, "manage_roles.html", {"users": users})
