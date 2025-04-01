from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, AppointmentMatch  
from .forms import EmployeeForm
from schedule_system.models import Schedule # 引入 Employee 模型
from django.views.generic import ListView
from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView
from django.http import JsonResponse, HttpResponseRedirect
from customer_system.models import CustomerProfile, CareAppointment
from django.contrib import messages




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

def customer_list(request):
    """查看所有客戶資料"""
    customers = CustomerProfile.objects.all()
    return render(request, "personnel_management/customer_list.html", {"customers": customers})

def customer_appointments(request, customer_id):
    """查看特定客戶的預約"""
    customer = get_object_or_404(CustomerProfile, id=customer_id)
    appointments = CareAppointment.objects.filter(user=customer.user)

    # 確保預約資料包含員工資料
    for appointment in appointments:
        # 若有配對到員工，將配對員工資料加入
        if appointment.employee:
            appointment.employee_name = appointment.employee.name
            appointment.employee_contact = appointment.employee.contact_number
        else:
            appointment.employee_name = None
            appointment.employee_contact = None

    return render(request, "personnel_management/customer_appointments.html", {
        "customer": customer,
        "appointments": appointments
    })



def match_appointment(request, appointment_id):
    appointment = get_object_or_404(CareAppointment, id=appointment_id, status="pending")

    # 找到符合預約時間的員工排班
    available_schedule = Schedule.objects.filter(
        start_datetime__lte=appointment.appointment_datetime,  # 開始時間 ≤ 預約時間
        end_datetime__gte=appointment.appointment_datetime  # 結束時間 ≥ 預約時間
    ).first()

    if available_schedule:
        # 檢查是否已經存在相同的配對紀錄
        existing_match = AppointmentMatch.objects.filter(appointment=appointment, schedule=available_schedule).first()

        if existing_match:
            # 如果已經配對過，則跳過創建配對
            return HttpResponseRedirect(
                f"{reverse('customer_appointments', args=[appointment.customer.id])}?status=already_matched"
            )

        # 建立配對紀錄
        match = AppointmentMatch.objects.create(
            appointment=appointment,
            schedule=available_schedule
        )

        # 更新預約狀態為「已確認」
        appointment.status = "confirmed"
        appointment.save()

        # 配對成功後重定向到客戶預約頁面，並傳遞成功參數
        return HttpResponseRedirect(
            f"{reverse('customer_appointments', args=[appointment.customer.id])}?status=success"
        )
    else:
        # 配對失敗後重定向到客戶預約頁面，並傳遞失敗參數
        return HttpResponseRedirect(
            f"{reverse('customer_appointments', args=[appointment.customer.id])}?status=fail"
        )
