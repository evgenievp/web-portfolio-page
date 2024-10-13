from django.db import models
from django.core.exceptions import ValidationError


def min_length_validator(value, min_length=5):
    if len(value) < min_length:
        raise ValidationError('Username has to be longer than 5 symbols')


class ApplicationModel(models.Model):
    DJANGO_APP = 'Django App'
    DATA_STRUCTURES = 'Data Structures'
    OTHER = 'Other'
    FLASK_APP = 'Flask Apps'

    APPLICATION_CHOICES = [
        (DJANGO_APP, 'Django App'),
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

    def __str__(self):
        return self.username


class AboutMeModel(models.Model):
    info = models.TextField(null=False)
