from django.forms import ModelForm
from web_page.main_page.models import ApplicationModel#, UserAccount
from django.contrib.auth import forms as auth_forms
from django import forms


class Project(ModelForm):
    class Meta:
        model = ApplicationModel
        fields = "__all__"


# class LoginForm(auth_forms.AuthenticationForm):
#     username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
#
