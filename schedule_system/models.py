from django.db import models
from django.contrib.auth.models import User
#from personnel_management.models import Employee  # 引入 Employee 模型
from django.apps import apps

class Schedule(models.Model):
    employee = models.ForeignKey(
        'personnel_management.Employee',  # 用 'app_label.ModelName' 避免循環導入
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)    #只用employee的話post抓不到user id，所以在加這行
    start_datetime = models.DateTimeField()  # 開始日期時間
    end_datetime = models.DateTimeField()    # 結束日期時間
    calendar_title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.employee} - {self.start_datetime} to {self.end_datetime}"

    @property
    def hours_worked(self):
        # 自動計算排班的工時數，將結果轉為小時
        duration = self.end_datetime - self.start_datetime
        return int(duration.total_seconds() / 3600)  # 工時，以小時為整數返回

    def get_employee(self):
        Employee = apps.get_model('personnel_management', 'Employee')  # 避免循環導入
        return Employee.objects.get(id=self.employee_id)