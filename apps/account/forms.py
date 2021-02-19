from django import forms
from .models import User



class LoginForm(forms.Form):
    """Формы авторизации на сайте"""
    email = forms.CharField(label='Email')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class UserProfileForm(forms.ModelForm):
    """Формы личного кабинета"""

    class Meta:
        model = User
        fields = ('email', 'user_phone')


class UserRegistrationForm(forms.ModelForm):
    """Формы регистрации на сайте"""

    class Meta:
        model = User
        fields = ('email',)

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)



