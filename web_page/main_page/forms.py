from django.forms import ModelForm
from web_page.main_page.models import ApplicationModel, UserAccount
from django import forms


class Project(forms.ModelForm):
    class Meta:
        model = ApplicationModel
        fields = "__all__"


class LoginForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['username', 'password']


class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['email', 'password', 'password']


