# customer_system/views.py
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomerProfile, CareAppointment
from .forms import CustomerProfileForm, CareAppointmentForm
from django.contrib import messages

@login_required
def customer_home(request):
    # 獲取用戶的所有預約，但排除已取消的預約
    appointments = CareAppointment.objects.filter(user=request.user).exclude(status="cancelled")

    return render(request, 'customer_system/customer_home.html', {'appointments': appointments})




@login_required
def customer_profile(request):
    """ 客戶資料填寫與顯示 """
    profile, created = CustomerProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = CustomerProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "客戶資料已成功儲存！")  # 提示訊息
            return redirect("customer_profile")  # 重新載入頁面，顯示最新資料
        else:
            messages.error(request, "請檢查輸入的資料是否正確。")
    else:
        form = CustomerProfileForm(instance=profile)

    return render(request, "customer_system/customer_profile.html", {"form": form, "profile": profile})



# 預約照護服務
@login_required
def book_care_service(request):
    if request.method == "POST":
        form = CareAppointmentForm(request.POST)
        if form.is_valid():
            # 讓客戶的預約跟 User 關聯
            care_appointment = form.save(commit=False)
            care_appointment.user = request.user  # 設置當前用戶為預約的客戶
            
            # 設定 customer 為當前用戶的 CustomerProfile
            customer_profile = CustomerProfile.objects.get(user=request.user)
            care_appointment.customer = customer_profile  # 關聯到 customer_profile

            care_appointment.save()

            messages.success(request, "您的預約已成功提交！")
            return redirect('customer_home')  # 提交成功後跳轉回首頁
    else:
        form = CareAppointmentForm()

    return render(request, "customer_system/book_care_service.html", {"form": form})


@login_required
def cancel_appointment(request, appointment_id):
    # 使用 get_object_or_404 來獲取對應的預約資料
    appointment = get_object_or_404(CareAppointment, id=appointment_id, user=request.user)

    if appointment.status == "pending":  # 只有待處理的預約可以取消
        appointment.status = "cancelled"
        appointment.save()
        messages.success(request, "您的預約已成功取消。")
    else:
        messages.error(request, "無法取消此預約。")

    return redirect("customer_home")