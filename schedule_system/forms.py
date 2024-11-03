from django import forms
from .models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['employee', 'start_datetime', 'end_datetime','calendar_title']
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # 取得當前用戶
        super(ScheduleForm, self).__init__(*args, **kwargs)
        if user and hasattr(user, 'employee'):
            # 固定設置為當前用戶的員工，並設為只讀
            self.fields['employee'].initial = user.employee
            self.fields['employee'].disabled = True