from django.shortcuts import render, redirect  
from personnel_management.models import Employee  # 引入 Employee 模型
from django.views import View
from .models import Schedule
from .forms import ScheduleForm
from django.contrib import messages


class ScheduleCreateView(View):
    def get(self, request):
        form = ScheduleForm()
        return render(request, 'schedule/create_schedule.html', {'form': form})

    def post(self, request):
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '排班已成功提交！')
        return render(request, 'schedule/create_schedule.html', {'form': form})
