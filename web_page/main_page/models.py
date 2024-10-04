from django.db import models


class DjangoApp(models.Model):
    title = models.CharField(max_length=50, null=False, unique=True)
    description = models.TextField(null=False)
    rate = models.IntegerField(default=0)
    url_link = models.TextField(unique=True, null=False)
