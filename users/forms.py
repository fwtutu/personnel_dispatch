from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):

    username = forms.CharField(label="使用者名稱", help_text="請輸入您的使用者名稱")
    email = forms.CharField(label="電子郵件", required=True, help_text="請輸入有效的電子郵件地址")
    password1 = forms.CharField(label="密碼", widget=forms.PasswordInput, help_text="請輸入密碼")
    password2 = forms.CharField(label="確認密碼", widget=forms.PasswordInput, help_text="再次輸入密碼以確認")



    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise ValidationError("此使用者名稱已存在，請選擇其他名稱")
        return username
    
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:  # 檢查是否輸入電子郵件
            raise forms.ValidationError("請輸入有效的電子郵件地址。")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        # 可以在這裡添加自訂邏輯，如果希望可以使用簡單密碼
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("兩次密碼輸入不一致")
        return password2

    def save(self, commit=True):
        user = User(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email']
        )

        user.set_password(self.cleaned_data['password1'])  # 設置密碼
        if commit:
            user.save()  # 保存用戶
        return user
