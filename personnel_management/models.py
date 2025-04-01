from django.db import models
from django.contrib.auth.models import User
from customer_system.models import CareAppointment
from schedule_system.models import Schedule



class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee', null=True)  # 添加外鍵關聯到 User
    name = models.CharField(max_length=100, blank=True)  # 允許為空
    age = models.IntegerField(null=True, blank=True)  # 允許為空
    contact_number = models.CharField(max_length=15, blank=True)  # 允許為空
    address = models.CharField(max_length=255, blank=True)  # 允許為空

    def __str__(self):
        return self.name or "未命名員工"

    # 當需要引用 CareAppointment 時，在方法或函數內進行延遲導入
    def get_appointments_for_employee(self):
        from customer_system.models import CareAppointment
        return CareAppointment.objects.filter(employee=self)

class AppointmentMatch(models.Model):
    appointment = models.OneToOneField(CareAppointment, on_delete=models.CASCADE, verbose_name="客戶預約")
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, unique=True,verbose_name="員工排班")
    matched_at = models.DateTimeField(auto_now_add=True, verbose_name="配對時間")

    def __str__(self):
        return f"預約 {self.appointment.id} 配對 員工 {self.schedule.employee.user.username}"
