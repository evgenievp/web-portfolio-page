from django.db import models
from django.core.exceptions import ValidationError


def min_length_validator(value, min_length=5):
    if len(value) < min_length:
        raise ValidationError('Username has to be longer than 5 symbols')



class ApplicationModel(models.Model):
    type_of_application = models.CharField(max_length=200, default='Django Apps')
    title = models.CharField(max_length=50, null=False, unique=True)
    description = models.TextField(null=False)
    url_link = models.TextField(unique=True, null=False)
    all_votes = models.IntegerField(default=0)



class UserAccount(models.Model):
    username = models.CharField(max_length=50,
                                null=False,
                                unique=True,
                                validators=[min_length_validator,]
                                )
    password = models.CharField(max_length=50,
                                null=False,
                                )

    email = models.EmailField(max_length=60,
                              unique=True,
                              null=False,
                              validators=[min_length_validator,],
                              )





