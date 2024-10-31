# 在 temp_worker/models.py
from django.db import models
from personnel_management.models import Employee  # 引入 Employee 模型
from users.models import User  # 引入 User 模型

class EmployeeProfile(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)  # 與 Employee 模型一對一關聯
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 與 User 模型一對一關聯
    # 可以添加其他個人檔案欄位
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.employee.name
