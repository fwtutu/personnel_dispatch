from django import forms
from django.db import models
from django.contrib.auth.models import User

class Rank(models.Model):
    ROLE_CHOICES = [
        ('customer', '客戶'),
        ('dispatcher', '派遣人員'),
        ('admin', '管理員'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='admin')

    def __str__(self):
        return self.user.username


