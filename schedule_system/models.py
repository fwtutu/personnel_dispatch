from django.db import models
from django.contrib.auth.models import User
from personnel_management.models import Employee  # 引入 Employee 模型

class Schedule(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()  # 開始日期時間
    end_datetime = models.DateTimeField()    # 結束日期時間

    @property
    def hours_worked(self):
        # 自動計算排班的工時數，將結果轉為小時
        duration = self.end_datetime - self.start_datetime
        return int(duration.total_seconds() / 3600)  # 工時，以小時為整數返回