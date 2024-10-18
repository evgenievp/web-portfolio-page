from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import CASCADE


def min_length_validator(value, min_length=5):
    if len(value) < min_length:
        raise ValidationError('Username has to be longer than 5 symbols')


class ApplicationModel(models.Model):
    DJANGO_APP = 'Django Apps'
    DATA_STRUCTURES = 'Data Structures'
    OTHER = 'Other'
    FLASK_APP = 'Flask Apps'

    APPLICATION_CHOICES = [
        (DJANGO_APP, 'Django Apps'),
        (DATA_STRUCTURES, 'Data Structures'),
        (OTHER, 'Other'),
        (FLASK_APP, 'Flask Apps'),
    ]

    type_of_application = models.CharField(
        max_length=20,
        choices=APPLICATION_CHOICES,
        default=DJANGO_APP,
    )
    title = models.CharField(max_length=50,
                             null=False,
                             unique=True,
                             )
    description = models.TextField(null=False)
    url_link = models.TextField(unique=True,
                                null=False,
                                )
    all_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


#
# class UserAccount(AbstractUser):
#     username = models.CharField(max_length=50,
#                                 null=False,
#                                 unique=True,
#                                 validators=[min_length_validator,]
#                                 )
#     password = models.CharField(max_length=150,
#                                 null=False,
#                                 )
#
#     email = models.EmailField(max_length=60,
#                               unique=True,
#                               null=False,
#                               validators=[min_length_validator,],
#                               )
#     voted = models.BooleanField(default=False)
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email', 'password']
#
#     def __str__(self):
#         return self.username
#


class User(models.Model):
    username = models.CharField(max_length=40, null=False)
    password = models.CharField(max_length=150, null=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']


class AboutMeModel(models.Model):
    info = models.TextField(null=False)
