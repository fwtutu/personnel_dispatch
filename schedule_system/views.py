from django.shortcuts import render, redirect  
from personnel_management.models import Employee  # 引入 Employee 模型
from django.views import View
from .models import Schedule
from .forms import ScheduleForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


class ScheduleCreateView(LoginRequiredMixin,View):
    login_url = '/user/login/'  # 如果未登入，重導向的登入頁面
    def get(self, request):
        form = ScheduleForm(user=request.user)
        return render(request, 'schedule/create_schedule.html', {'form': form})

    def post(self, request):

        form = ScheduleForm(request.POST,user=request.user)
        if form.is_valid():
            schedule = form.save(commit=False)     
            schedule.user = request.user  # #只用employee的話抓不到user id，所以在加這行
            schedule.employee = request.user.employee   # 將排班記錄的員工設置為當前使用者
            schedule.save()
            messages.success(request, '排班已成功提交！')
        return render(request, 'schedule/create_schedule.html', {'form': form})


class UserScheduleListView(LoginRequiredMixin, ListView):
    model = Schedule
    template_name = 'schedule/user_schedule_list.html'  # 新模板路徑
    context_object_name = 'schedules'
    paginate_by = 10  # 每頁顯示 10 筆排班

    def get_queryset(self):
        return Schedule.objects.filter(employee=self.request.user.employee).order_by('start_datetime')
