from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'age', 'contact_number', 'address']  # 包含所有需要更新的字段
