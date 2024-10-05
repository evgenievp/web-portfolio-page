from django.db import models


class ApplicationModel(models.Model):
    type_of_application = models.CharField(max_length=200, unique=True, default='Django Apps')
    title = models.CharField(max_length=50, null=False, unique=True)
    description = models.TextField(null=False)
    rate = models.FloatField(default=0)
    url_link = models.TextField(unique=True, null=False)
    all_votes = models.IntegerField(default=0)


