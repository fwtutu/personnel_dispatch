from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 連接 Django 內建用戶
    name = models.CharField(max_length=100, verbose_name="姓名")
    contact_number = models.CharField(max_length=15, verbose_name="電話")
    address = models.TextField(verbose_name="住址")
    service_time = models.DateTimeField(default=now, verbose_name="服務時間")  # 自動填入當前時間

    def __str__(self):
        return self.name


class CareAppointment(models.Model):
    STATUS_CHOICES = [
        ('pending', '待處理'),
        ('confirmed', '已確認'),
        ('cancelled', '已取消')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')  # 仍然保留 user 欄位
    # 新增 customer 欄位
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='careappointments')  # 使用 CustomerProfile 作為外鍵
    care_location = models.CharField(max_length=255, verbose_name="預約地點")
    appointment_datetime = models.DateTimeField(verbose_name="預約時間")
    special_requirements = models.TextField(blank=True, null=True, verbose_name="特別需求")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="狀態")
    employee = models.ForeignKey('personnel_management.Employee', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.customer.name} - {self.appointment_datetime} ({self.get_status_display()})"
