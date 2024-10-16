from django.forms import ModelForm
from web_page.main_page.models import ApplicationModel, UserAccount
from django.contrib.auth import forms as auth_forms
from django import forms

class Project(ModelForm):
    class Meta:
        model = ApplicationModel
        fields = "__all__"


class LoginForm(auth_forms.AuthenticationForm):
    class Meta:
        model = UserAccount
        fields = ['username', 'password']
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(ModelForm):
    class Meta:
        model = UserAccount
        fields = '__all__'

    password = forms.CharField(widget=forms.PasswordInput)