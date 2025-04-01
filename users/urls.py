from django.urls import path
from .views import users_home, logout_view, manage_roles, register, login_view, login_success ,register_customer

urlpatterns = [
    path("", users_home, name="users_home"),  # 首頁路由
    path("register/", register, name="register"),
    path("register_employee/", register, name="register_employee"),
    path("login/", login_view, name="login"),
    path("login_customer/", login_view, name="login_customer"),
    path("login_success/", login_success, name="login_success"),  # 登入成功頁面
    path("logout/", logout_view, name="logout"),
    path("manage_roles/", manage_roles, name="manage_roles"),
    path("register_customer/", register_customer, name="register_customer"),
]
