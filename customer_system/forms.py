from django import forms
from .models import CustomerProfile, CareAppointment  
from django.utils import timezone


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['name', 'contact_number', 'address']
        labels = {
            'name': '姓名',
            'contact_number': '電話',
            'address': '住址',
        }


class CareAppointmentForm(forms.ModelForm):
    care_location = forms.CharField(
        label="預約地點",
        help_text="請輸入您希望照護的地址"
    )
    
    appointment_datetime = forms.DateTimeField(
        label="預約日期與時間",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        help_text="請選擇預約的時間"
    )
    
    special_requirements = forms.CharField(
        label="特別需求",
        required=False,
        widget=forms.Textarea(attrs={"rows": 3}),
        help_text="請輸入您對照服員的特別需求 (選填)"
    )

    class Meta:
        model = CareAppointment
        fields = ['care_location', 'appointment_datetime', 'special_requirements']