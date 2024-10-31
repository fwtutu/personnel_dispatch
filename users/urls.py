from django.urls import path
from .views import home, logout_view, manage_roles, register, login_view, login_success

urlpatterns = [
    path("", home, name="home"),  # 首頁路由
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("login_success/", login_success, name="login_success"),  # 登入成功頁面
    path("logout/", logout_view, name="logout"),
    path("manage_roles/", manage_roles, name="manage_roles"),
]
