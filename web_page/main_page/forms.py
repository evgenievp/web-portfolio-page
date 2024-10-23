from django.forms import ModelForm
from web_page.main_page.models import ApplicationModel, User, Message
from django.contrib.auth import forms as auth_forms
from django import forms


class Project(ModelForm):
    class Meta:
        model = ApplicationModel
        fields = "__all__"


class LoginForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(widget=forms.TextInput(attrs={'autofocus': True, "placeholder": "username"}))
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = "Username"
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['username'].error_messages = {'required': '', 'label': None}
        self.fields['password'].error_messages = {'required': '', 'label':  None}

    class Meta:
        model = User
        help_texts = {
            'username': "",
            'password': '',
        }
        label = {
            'username': '',
            'password': '',
        }


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'If you wish - attack title here.'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Only I will be able to see the messages submitted here.'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].label = ''
