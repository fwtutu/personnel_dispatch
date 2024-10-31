from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee', null=True)  # 添加外鍵關聯到 User
    name = models.CharField(max_length=100, blank=True)  # 允許為空
    age = models.IntegerField(null=True, blank=True)  # 允許為空
    contact_number = models.CharField(max_length=15, blank=True)  # 允許為空
    address = models.CharField(max_length=255, blank=True)  # 允許為空

    def __str__(self):
        return self.name or "未命名員工"
