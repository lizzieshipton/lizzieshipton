from __future__ import unicode_literals

from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    detail = models.CharField(max_length=1000)
    url = models.URLField()
    thumbnail = models.CharField(max_length=200)
