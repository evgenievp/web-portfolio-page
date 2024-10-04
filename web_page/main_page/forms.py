from django.forms import ModelForm
from web_page.main_page.models import DjangoApp


class Project(ModelForm):
    class Meta:
        model = DjangoApp
        fields = "__all__"


