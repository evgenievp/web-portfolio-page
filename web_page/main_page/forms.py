from django.forms import ModelForm
from web_page.main_page.models import ApplicationModel
from django import forms


class Project(forms.ModelForm):
    class Meta:
        model = ApplicationModel
        fields = "__all__"



